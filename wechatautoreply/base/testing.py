# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from http_request import BaseRequestApi
from settings import settings

class TestRequestApi(BaseRequestApi):
    HOST = "127.0.0.1:" + str(settings['PORT'])


class BaseTestCase(unittest.TestCase):

    RequestApi = TestRequestApi

    def assert200(self, resp):
        self.assertTrue(resp.status == 200)

    def assert404(self, resp):
        self.assertTrue(resp.status == 404)

    def setUp(self):
        print "test start"

    def tearDown(self):
        print 'test stop'