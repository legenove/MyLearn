# -*- coding: utf-8 -*-
from core.handler import RequestHandler


class ApiHandler(RequestHandler):
    on_initialize_decorators = []

    def on_finish(self):
        print 'test finish'