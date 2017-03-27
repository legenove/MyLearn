# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import threading
from redis import Redis
import logging
import requests

try:
    redis_settings = settings.redis_settings
except:
    redis_settings = {
        "REDIS_BACKEND": {"servers": 'localhost', "port": 6379, "db": 4,
                          'password': ''},
        "MQUEUE_BACKEND": {"servers": 'localhost', "port": 6379, "db": 12,
                           'password': ''},
        "Redis_Source_Use_MongoDB": False  # if redis down use mongodb
    }


class RedisClient(object):
    instance = None
    locker = threading.Lock()

    def __init__(self):
        """ intialize the client of redis  include port db and servers """
        try:
            config = redis_settings["REDIS_BACKEND"]
            self.servers = config["servers"]
            self.port = config["port"]
            self.db = config["db"]
            self.password = config["password"]
            # r = redis.Redis('10.66.136.84', '6379', 0,password="xsw2CDE#vfr4")
            #r = redis.Redis('10.66.136.84', '6379', 0)
            self.redis = Redis(self.servers, self.port, self.db,
                               password=self.password, socket_timeout=1)
        except Exception, e:
            print "Redis YAMLConfig Error :", e
            logging.error(e)


    @classmethod
    def getInstance(klass):
        """
        get the instance of RedisClient
        return:
            the redis client
        """
        klass.locker.acquire()
        try:
            if not klass.instance:
                klass.instance = klass()
            return klass.instance
        finally:
            klass.locker.release()

    def reconnect(self):
        """
        if the connetion is disconnet  then connect again
        """
        try:
            self.redis = Redis(self.servers, self.port, self.db)
        except Exception, e:
            print e

redis = RedisClient.getInstance().redis


class RedisPipeline(object):
    instance = None
    locker = threading.Lock()

    def __init__(self):
        self.pipeline = redis.pipeline()

    @classmethod
    def getInstance(cls):
        """
        get the instance of RedisClient Pipeline
        return:
            the redis client pipelint
        """
        cls.locker.acquire()
        try:
            if not cls.instance:
                cls.instance = cls()
            return cls.instance
        finally:
            cls.locker.release()


class Model(object):
    __pipeline__ = None

    def __init__(self):
        # self._get_piple()
        pass


class RedisCommon(object):

    _p = None

    @property
    def pipeline(self):
        if self._p is None:
            self._p = RedisPipeline.getInstance().pipeline
        return self._p


class RTest(Model, RedisCommon):
    pass


class RTest2(Model, RedisCommon):
    pass


# print id(RTest.pipeline)
print id(RTest.pipeline)

a = RTest()
print id(a.pipeline)
b = RTest()
print id(b.pipeline)

print id(RTest2.pipeline)

a = RTest2()
print id(a.pipeline)
b = RTest2()
print id(b.pipeline)

print b.pipeline
