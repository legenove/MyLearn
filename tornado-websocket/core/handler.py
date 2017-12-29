# -*- coding: utf-8 -*-
import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    on_initialize_decorators = []
    def initialize(self):
        request = self.request
        meth = getattr(self, self.request.method.lower(), None)
        if meth is None and self.request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method

        for decorator in self.on_initialize_decorators:
            meth = decorator(meth)

        setattr(self, self.request.method.lower(), meth)