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

class WeChatPortalTestCase(BaseTestCase):
    @staticmethod
    def _generate_signature(message):
        keylist = message.values()
        keylist.sort()
        signature = ''.join(map(str, keylist))
        return sha1(signature).hexdigest()

    @staticmethod
    def _generate_nonce():
        return random.randrange(10000000000)

    @staticmethod
    def _generate_echostr():
        echostr = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))
        return echostr

    def setUp(self):
        self.server = Server
        print "test start"

    def tearDown(self):
        print 'test stop'

    def testWeChatPortal(self):
        timestamp = int(time())
        nonce = self._generate_nonce()
        echostr = self._generate_echostr()
        token = self.server.token
        message = {
            'token': token,
            'timestamp': timestamp,
            'nonce': nonce, }

        path = '/wechat/'

        # 正确验证
        params = {
            'signature': self._generate_signature(message),
            'timestamp': timestamp,
            'nonce': nonce,
            'echostr': echostr
        }
        resp = self.RequestApi.get(path, params)
        self.assert200(resp)
        self.assertTrue(resp.read() == echostr)

        # 缺少参数
        params = {
            'signature': self._generate_signature(message),
            'timestamp': timestamp,
            'nonce': nonce,
        }
        resp = self.RequestApi.get(path, params)
        self.assert404(resp)

        # token 错误
        wrong_message = {'token': self._generate_echostr(),
                         'timestamp': timestamp,
                         'nonce': nonce, }
        params = {
            'signature': self._generate_signature(wrong_message),
            'timestamp': timestamp,
            'nonce': nonce,
            'echostr': echostr
        }
        resp = self.RequestApi.get(path, params)
        self.assert404(resp)

if __name__ == "__main__":
    unittest.main()
