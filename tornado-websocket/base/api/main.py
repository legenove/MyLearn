# -*- coding: utf-8 -*-
from . import ApiHandler


class MainRequestHandler(ApiHandler):
    def get(self):
        self.write('hello world')