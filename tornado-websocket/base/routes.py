# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .api.main import MainRequestHandler

routes = [
    dict(resource=MainRequestHandler, urls=['/'], endpoint='main'),
]