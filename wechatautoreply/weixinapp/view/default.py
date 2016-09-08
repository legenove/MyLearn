# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import os
import logging
from lxml import etree
from time import time
from datetime import datetime
from hashlib import sha1

_sha1 = lambda x: sha1(x).hexdigest()


def check_signature(message):
    signature = message.pop('signature')
    logging.debug('[_check_signature]> signature: %s' % signature)
    logging.debug(message)

    value_list = message.values()
    value_list.sort()
    logging.debug(value_list)
    compare = ''.join(map(str, value_list))

    other_keylist = ['timestamp', 'nonce', 'token']
    other_compare = ''.join([str(message[key]) for key in other_keylist])
    return signature == _sha1(compare) or signature == _sha1(other_compare)


def get_message_data(xml):
    """解析xml 提取其中数据 并存入一个dict"""
    data_dict = {}

    for node in xml.iter():
        data_dict[node.tag] = node.text
    return data_dict


def check_xml_wf(xml):
    """ 使用lxml.etree.parse 检测xml是否符合语法规范"""
    # 参数xml是经过StringIO处理过的instance类型
    try:
        xml = etree.parse(xml)
        return xml
    except etree.XMLSyntaxError, e:
        logging.debug(
            '[返回数据]:This %s \n is NOT a weill-formed xml!! %s' % (xml, e))
        return False


class WXContent(object):
    TEXT_TPL = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
            <FuncFlag>0</FuncFlag>
        </xml>
        """

    PIC_TPL = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[image]]></MsgType>
            <Image>
            <MediaId><![CDATA[{media_id}]]></MediaId>
            </Image>
        </xml>
        """

    VOICE_TPL = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[voice]]></MsgType>
            <Voice>
            <MediaId><![CDATA[{media_id}]]></MediaId>
            </Voice>
        </xml>
        """

    VIDEO_TPL = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[video]]></MsgType>
            <Video>
            <MediaId><![CDATA[{media_id}]]></MediaId>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{content}]]></Description>
            </Video>
        </xml>
        """
    MUSIC_TPL = """<xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{description}]]></Description>
            <MusicUrl><![CDATA[{music_url}]]></MusicUrl>
            <HQMusicUrl><![CDATA[{hq_music_url}]]></HQMusicUrl>
            <ThumbMediaId><![CDATA[{media_id}]]></ThumbMediaId>
        </Music>
        </xml>
        """
    # 图文信息
    ARTICLE_TPL_HEAD = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>{article_count}</ArticleCount>
            <Articles>
                {articles}
            </Articles>
            <FuncFlag>0</FuncFlag>
        </xml>
        """

    ARTICLE_ITEM = '''
        <item>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{content}]]></Description>
            <PicUrl><![CDATA[{pic_url}]]></PicUrl>
            <Url><![CDATA[{url}]]></Url>
        </item>
        '''