# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import importlib

from os import path, environ as _env

url_prefix = '/test'

settings = {
    'DEBUG': False,
    'TESTING': False,
    'PORT': 8888
}


def load_settings(config):
    config.update(**settings)
    try:
        from .routes import routes
        config.update_uri(routes, url_prefix)
    except:
        pass
