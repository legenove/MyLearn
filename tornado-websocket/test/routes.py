# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .api.index import IndexRequestHandler

routes = [
    dict(resource=IndexRequestHandler, urls=['/'], endpoint='index'),
]