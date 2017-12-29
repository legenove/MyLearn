# -*- coding: utf-8 -*-
from . import ApiHandler


class IndexRequestHandler(ApiHandler):
    def get(self):
        self.write('hello world')