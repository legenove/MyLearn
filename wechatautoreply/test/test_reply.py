# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import random
import unittest
import urllib

from time import time
from hashlib import sha1

from weixinapp.models.servers import Server
from base.testing import BaseTestCase

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class WeChatReplyTestCase(BaseTestCase):
    def setUp(self):
        self.server = Server
        self.message = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[指南]]></Content>
        </xml>
        '''

        self.message1 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_text]]></Content>
        </xml>
        '''

        self.message2 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_image]]></Content>
        </xml>
        '''

        self.message3 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_voice]]></Content>
        </xml>
        '''

        self.message4 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_video]]></Content>
        </xml>
        '''

        self.message5 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_music]]></Content>
        </xml>
        '''

        self.message6 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[test_news]]></Content>
        </xml>
        '''

        self.message7 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[测试_?ab]]></Content>
        </xml>
        '''

        self.message8 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[数死早]]></Content>
        </xml>
        '''

        self.message9 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[subscribe]]></Event>
            <EventKey><![CDATA[]]></EventKey>
        </xml>
        '''

        self.message10 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[b]]></Content>
        </xml>
        '''

        self.message11 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Content><![CDATA[unsubscribe]]></Content>
        </xml>
        '''

        self.message12 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[image]]></MsgType>
            <Content><![CDATA[unsubscribe]]></Content>
        </xml>
        '''

        self.message13 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[location]]></MsgType>
            <Content><![CDATA[unsubscribe]]></Content>
        </xml>
        '''

        self.message14 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[series]]></Content>
        </xml>
        '''

        self.message15 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[a]]></Content>
        </xml>
        '''

        self.message17 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[1231231123]]></Content>
        </xml>
        '''

        self.message16_wrong = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[男]]></Content>
        </xml>
        '''

        self.message16 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[m]]></Content>
        </xml>
        '''

        self.message18 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[白痴]]></Content>
        </xml>
        '''

        self.message19 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[over]]></Content>
        </xml>
        '''

        self.message20 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser2]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[series]]></Content>
        </xml>
        '''

        self.message21 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser2]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[a]]></Content>
        </xml>
        '''

        self.message23 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser2]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[1231123]]></Content>
        </xml>
        '''

        self.message22 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser2]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[f]]></Content>
        </xml>
        '''

        self.message24 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[event]]></MsgType>
            <Event><![CDATA[CLICK]]></Event>
            <EventKey><![CDATA[测试_opinion]]></EventKey>
        </xml>
        '''

        self.message25 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[换一个]]></Content>
        </xml>
        '''

        self.message26 = '''
        <xml>
            <ToUserName><![CDATA[toUser]]></ToUserName>
            <FromUserName><![CDATA[fromUser2]]></FromUserName>
            <CreateTime>1348831860</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[换一个]]></Content>
        </xml>
        '''

        self.path = '/wechat/'
        print "test start"

    def tearDown(self):
        print 'test stop'


    def test_main(self):
        # 测试指南页面
        message = self.message
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_text(self):
        message = self.message1
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_image(self):
        message = self.message2
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_voice(self):
        message = self.message3
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_video(self):
        message = self.message4
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_music(self):
        message = self.message5
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)

    def test_news(self):
        message = self.message6
        resp = self.RequestApi.post_body_request(self.path, message)
        print resp.read()
        self.assert200(resp)


if __name__ == "__main__":
    unittest.main()
