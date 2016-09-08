# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os import path, environ as _env
from urlparse import urlparse


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

    DEBUG = False
    TESTING = False


config = Config()
