# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib
import sys

from flask import Flask

from os import path, environ as _env
from urlparse import urlparse

settings = {
    'DEBUG': False,
    'TESTING': False,
    'PORT': 5000
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

    def update(self, **kw):
        for name, value in kw.items():
            self.__setattr__(name, value)


def create_app(register_bp=True, test=False, *modules):
    app = Flask(__name__, static_folder='static')
    config = Config()
    load_flask_settings(app, config, *modules)
    if test:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
    if register_bp:
        load_flask_blueprints(app, *modules)
    return app


def load_flask_blueprints(app, *modules):
    kwargs = {}
    mods = []

    for module in modules:
        try:
            if module == 'base':
                continue
            mods.append(importlib.import_module('%s.registers' % module))
        except ImportError, err:
            raise ImportError("Could not import settings '%s' (Is it on sys.path?): %s" % (module, err))

    for mod in mods:
        if hasattr(mod, 'register_blueprints'):
            getattr(mod, 'register_blueprints')(app, **kwargs)

        if hasattr(mod, 'register_extensions'):
            getattr(mod, 'register_extensions')(app, **kwargs)

        if hasattr(mod, 'register_after_request'):
            getattr(mod, 'register_after_request')(app, **kwargs)


def load_flask_settings(app, config, *modules):
    settings.update({'MODULES': modules})
    kwargs = {}
    mods = []

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

    app.config.from_object(config)


def load_settings(config):
    config.update(**settings)
