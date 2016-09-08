# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import os
import logging
from time import time, sleep
from datetime import datetime
from hashlib import sha1
from StringIO import StringIO

from flask import views
from flask import abort, request
from flask import current_app

from forms import WeixinConnectForm
from default import check_signature, get_message_data, check_xml_wf
from default import WXContent

from weixinapp.models.servers import Server
# from manage import app


class WeChatRequest(object):
    def __init__(self, from_user_name, to_user_name,
                 content, is_event, server):
        self.from_user_name = from_user_name
        self.to_user_name = to_user_name
        self.content = content
        self.context_reply_id = 0
        self.cur_rule = None
        self.rule_type = ''
        self.reply_count = -3
        self.is_event = is_event
        self.server = server

    def get_replies(self):
        # TODO: get replies from other server
        replies = []
        self.reply_type = 'text'
        return replies

    def reply_message(self):
        test = current_app.config.get('TESTING', False)
        user_info = {}
        user_info['ToUserName'] = self.from_user_name
        user_info['FromUserName'] = self.to_user_name
        user_info['CreateTime'] = int(time())
        replies = self.get_replies()
        if not test and not replies:
            return ''

        if not isinstance(replies, list):
            replies = [replies]
        if test:
            self.test_content(replies)
            if not replies:
                return ''

        if self.reply_type == 'text':
            user_info.update(replies[0])
            xml = WXContent.TEXT_TPL.format(**user_info)
        elif self.reply_type == 'voice':
            user_info.update(replies[0])
            xml = WXContent.VOICE_TPL.format(**user_info)
        elif self.reply_type == 'image':
            user_info.update(replies[0])
            xml = WXContent.PIC_TPL.format(**user_info)
        elif self.reply_type == 'video':
            user_info.update(replies[0])
            xml = WXContent.VIDEO_TPL.format(**user_info)
        elif self.reply_type == 'music':
            user_info.update(replies[0])
            xml = WXContent.MUSIC_TPL.format(**user_info)
        elif self.reply_type == 'news':
            article_body = ''
            for reply in replies:
                article_item = WXContent.ARTICLE_ITEM.format(**reply)
                article_body += article_item

            user_info.update({
                'articles': article_body,
                'article_count': len(replies)})
            xml = WXContent.ARTICLE_TPL_HEAD.format(**user_info)

        if check_xml_wf(StringIO(xml)):
            return xml
        else:
            return ''

    def test_content(self, replies):
        if self.content.startswith('test'):
            try:
                self.reply_type = self.content.split('_')[1]
            except IndexError:
                pass
            if self.reply_type == 'text':
                replies.append({'content': '测试text'+'\n'+"测试换行"})
            elif self.reply_type == 'voice':
                replies.append({'media_id': 'test_voice_123456'})
            elif self.reply_type == 'image':
                replies.append({'media_id': 'test_image_123456'})
            elif self.reply_type == 'video':
                replies.append({'media_id': 'test_video_123456',
                                'title': 'test_video_title',
                                'content': 'test_video', })
            elif self.reply_type == 'music':
                replies.append({'media_id': 'test_music_123456',
                                'title': 'test_music_title',
                                'description': 'test_music_desc',
                                'hq_music_url': 'test_hq_music_url',
                                'music_url': 'test_music_url', })
            elif self.reply_type == 'news':
                replies.append({'pic_url': 'test_article_0_pic_url',
                                'title': 'test_article_0_title',
                                'content': 'test_article_0',
                                'url': 'test_article_0_url', })
                replies.append({'pic_url': 'test_article_1_pic_url',
                                'title': 'test_article_1_title',
                                'content': 'test_article_1',
                                'url': 'test_article_1_url', })
                replies.append({'pic_url': 'test_article_2_pic_url',
                                'title': 'test_article_2_title',
                                'content': 'test_article_2',
                                'url': 'test_article_2_url', })
            else:
                self.reply_type = 'text'
                replies.append({'content': '没有测试'})


class WeChatReply(views.MethodView):
    RequestClass = WeChatRequest

    def get(self, id):
        self.server = Server
        if not self.server:
            return ''
        logging.debug('再次验证接口是否接通')
        echoStr = self._portal()
        logging.debug('接口验证通过')
        return echoStr

    def post(self, id):
        self.server = Server
        if not self.server:
            return ''
        result = ''
        xml_str = self._get_xml()
        if xml_str is False:
            return result
        message_dict = get_message_data(xml_str)
        try:
            to_user_name = message_dict['ToUserName']
            from_user_name = message_dict['FromUserName']
            content = message_dict.get('Content', '').strip()
            # event = message_dict.get('Event', '').strip()
            # event_key = message_dict.get('EventKey', '').strip()
            message_type = message_dict['MsgType']

            is_event = message_type == 'event'
            weixin_req = self.RequestClass(
                from_user_name, to_user_name, content, is_event, self.server)
        except KeyError, e:
            logging.debug('[返回数据]:获取的消息数据有错误: %s ' % e)
            logging.debug(message_dict)
            return result

        # message_type
        # :text
        # :image
        # :voice
        # :video
        # :shortvideo
        # :location
        # :link
        # :event
        # # Event
        # :subscribe   :unsubscribe
        # :CLICK
        # :SCAN
        #   :LOCATION
        #   :VIEW

        if message_type == 'text':
            result = weixin_req.reply_message()
        # elif message_type == 'event':
        # if event == 'subscribe':
        #         result = weixin_req.reply_message()
        #     elif event == 'CLICK':
        #         result = weixin_req.reply_message()
        else:
            logging.debug(
                '[返回数据]:消息格式无法处理！！ MsgType: %s' % message_type)

        return result

    def _portal(self):
        if request.method != 'GET':
            abort(404)

        get_params = WeixinConnectForm(request.args, csrf_enabled=False)
        if not get_params.validate():
            logging.error("验证信息错误 %s" % request.args)
            abort(404)

        message = get_params.data
        echostr = message.pop('echostr')
        message['token'] = self.server.token
        if not check_signature(message):
            logging.error("_check_signature 错误!!")
            abort(404)

        return echostr

    def _get_xml(self):
        if request.method != "POST":
            logging.debug(
                "[返回数据]:Request Method ERROR!! %s" % request.method)
            return False

        postStr = request.data

        xml = StringIO(postStr)
        check_xml = check_xml_wf(xml)
        if check_xml:
            return check_xml
        else:
            logging.debug("得到的post信息不是xml信息")
            return False