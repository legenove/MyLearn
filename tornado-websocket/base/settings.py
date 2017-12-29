# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import importlib

from os import path, environ as _env

settings = {
    'DEBUG': False,
    'TESTING': False,
    'PORT': 8888
}

class CalypsoEnv(object):
    # 线上环境用Calypso 配置，所以做一个environ 的代理
    def get(self, key, default=None):
        value = _env.get(key)

        # 相当于重定向
        alias = _env.get(value)
        if alias is not None:
            return alias

        if not value and default:
            return default
        return value


environ = CalypsoEnv()


class EnvConfigType(type):
    def __getattribute__(cls, key):
        value = object.__getattribute__(cls, key)
        env = environ.get(key)

        if env is not None:
            value = type(value)(env)
        return value


class Config(object):
    __metaclass__ = EnvConfigType

    URIS = []
    ROUTES = []

    def update(self, **kw):
        for name, value in kw.items():
            self.__setattr__(name, value)

    def update_uri(self, routes, url_prefix=''):
        self.ROUTES.extend(routes)
        self.URIS.extend([(url_prefix + r['urls'][0], r['resource'])for r in routes])

def load_tornado_settings(*modules):
    settings.update({'MODULES': modules})
    kwargs = {}
    mods = []
    config = Config()

    for module in modules:
        try:
            mods.append(importlib.import_module('%s.settings' % module))
        except ImportError, err:
            raise ImportError("Could not import settings '%s' (Is it on sys.path?): %s" % (module, err))

    for module in modules:
        try:
            mods.append(importlib.import_module('%s.my_settings' % module))
        except ImportError:
            pass

    for mod in mods:
        if hasattr(mod, 'load_settings'):
            getattr(mod, 'load_settings')(config, **kwargs)

    return config


def load_settings(config):
    config.update(**settings)
    try:
        from .routes import routes
        config.update_uri(routes)
    except:
        pass