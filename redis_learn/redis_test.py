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


import inspect
import functools


def redis_keys(key_format, extkws={}):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            from copy import deepcopy
            def get_kws(k_dic, kws, v=None):
                if v is None:
                    v = {}
                if k_dic:
                    k = k_dic.keys()[0]
                    if isinstance(k_dic[k], list):
                        for ki in k_dic.pop(k):
                            v[k] = ki
                            get_kws(k_dic, kws, v)
                            v.pop(k)
                    else:
                        v[k] = k_dic.pop(k)
                        get_kws(k_dic, kws, v)
                else:
                    kws.append(deepcopy(v))

            def _format(**kwargs):
                kws = []
                get_kws(kwargs, kws)
                keys = [key_format.format(**kw) for kw in kws]
                if len(keys) == 1:
                    return keys[0]
                else:
                    return keys

            arg_names, varargs, varkw, defaults = inspect.getargspec(func)
            # defaults
            _defargs = dict(
                zip(arg_names[-len(defaults):], defaults)) if defaults else {}
            _args1 = dict(zip(arg_names, args))
            _kwds = dict(_defargs, **_args1)
            _kwds.update(kwargs)
            _kwds.update(extkws)
            ckey = key_format
            import re

            pattern = r"(\{.*?\})"
            guid = re.findall(pattern, key_format, re.M)
            cut_down = lambda x: x.replace('{', '').replace('}', '')
            if len(guid) > 0:
                cache_keys_dict = {cut_down(g):
                                       _kwds.get(cut_down(g), '')
                                   for g in guid}
                ckey = _format(**cache_keys_dict)
            kwargs['rkey'] = ckey
            return func(*args, **kwargs)
        wrapper.original_function = func
        wrapper.func_name = func.func_name
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator


class ExpireTime(object):
    HALF_MIN = 30
    MIN = 60
    FIVE_MINS = 60 * 5
    TEN_MINS = 60 * 10
    TWENTY_MINS = 60 * 20
    HALF_HOUR = 60 * 30
    HOUR = 60 * 60
    HALF_DAY = 60 * 60 * 12
    DAY = 60 * 60 * 24
    TWO_DAY = 60 * 60 * 48
    MONTH_DAY = 60 * 60 * 24 * 30


class RedisPipeline(object):
    instance = None
    locker = threading.Lock()

    def __init__(self):
        self.pipeline = RedisClient.getInstance().redis.pipeline()

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


class RedisBaseOp(object):
    key_tpl = None
    extkws = {}
    result = None
    pipeline = RedisPipeline.getInstance().pipeline

    def _set_key(self, *args, **kwargs):
        self.expire_time = kwargs.get('expire', ExpireTime.MONTH_DAY)
        self.key = kwargs.get('rkey')
        print self.key

    def set_key(self, *args, **kwargs):
        redis_keys(self.key_tpl, self.extkws)(self._set_key)(*args, **kwargs)

    @property
    def db(self):
        if self.pipeline:
            return self.pipeline
        else:
            self.pipeline = RedisPipeline.getInstance().pipeline
        return self.pipeline

    def __getattribute__(self, attr):
        if attr in object.__getattribute__(self, 'OPTION_METHODS'):
            return functools.partial(
                getattr(object.__getattribute__(self, 'db'), attr), self.key)
        else:
            return object.__getattribute__(self, attr)

    def commit(self):
        self.result = self.db.execute()
        return self.result

    OPTION_METHODS = []


class SortedSet(RedisBaseOp):
    def add(self, *args, **kwargs):
        """Adds *args, **kwargs to the set."""
        self.zadd(*args, **kwargs)

    def remove(self, *member):
        """Removes *member from set."""
        self.zrem(*member)

    def incr_by(self, member, amount=1):
        """Increments the member by increment."""
        self.zincrby(member, amount)

    def rank(self, member):
        """Return the rank (the index) of the element."""
        return self.zrank(member)

    def revrank(self, member):
        """Return the rank of the member in reverse order."""
        return self.zrevrank(member)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.zrange(index.start, index.stop)
        else:
            return self.zrange(index, index)[0]

    def score(self, member):
        """Returns the score of member."""
        return self.zscore(member)

    def __len__(self):
        return self.zcard()

    def __contains__(self, val):
        return self.zscore(val) is not None

    @property
    def members(self):
        """Returns the members of the set."""
        return self.zrange(0, -1)

    @property
    def revmembers(self):
        """Returns the members of the set in reverse."""
        return self.zrevrange(0, -1)

    def __iter__(self):
        return self.members.__iter__()

    def __reversed__(self):
        return self.revmembers.__iter__()

    def __repr__(self):
        return "<%s '%s' %s>" % (self.__class__.__name__, self.key,
                                 self.members)

    @property
    def _min_score(self):
        return self.zscore(self.__getitem__(0))

    @property
    def _max_score(self):
        return self.zscore(self.__getitem__(-1))

    def lt(self, v, limit=None, offset=None):
        """Returns the list of the members of the set that have scores
        less than v.
        """
        if limit is not None and offset is None:
            offset = 0
        return self.zrangebyscore(self._min_score, "(%f" % v,
                                  start=offset, num=limit, withscores=True)

    def le(self, v, limit=None, offset=None):
        """Returns the list of the members of the set that have scores
        less than or equal to v.
        """
        if limit is not None and offset is None:
            offset = 0
        return self.zrangebyscore(self._min_score, v,
                                  start=offset, num=limit)

    def gt(self, v, limit=None, offset=None):
        """Returns the list of the members of the set that have scores
        greater than v.
        """
        if limit is not None and offset is None:
            offset = 0
        return self.zrangebyscore("(%f" % v, self._max_score,
                                  start=offset, num=limit)

    def ge(self, v, limit=None, offset=None):
        """Returns the list of the members of the set that have scores
        greater than or equal to v.
        """
        if limit is not None and offset is None:
            offset = 0
        return self.zrangebyscore("(%f" % v, self._max_score,
                                  start=offset, num=limit)

    def between(self, min, max, limit=None, offset=None):
        """Returns the list of the members of the set that have scores
        between min and max.
        """
        if limit is not None and offset is None:
            offset = 0
        return self.zrangebyscore(min, max,
                                  start=offset, num=limit)

    def eq(self, value):
        """Returns the list of the members of the set that have scores
        equal to value.
        """
        return self.zrangebyscore(value, value)

    OPTION_METHODS = ['zadd', 'zrem', 'zincrby', 'zrank',
                            'zrevrank', 'zrange', 'zrevrange', 'zrangebyscore',
                            'zcard',
                            'zscore', 'zremrangebyrank', 'zremrangebyscore']


class RecommendActivityRedis(SortedSet):
    key_tpl = 'recommend:activity:{day}:{week}'

    def __init__(self, day, week):
        self.set_key(day=day, week=week)


class RecommendAllRedis(SortedSet):
    key_tpl = 'recommend:all_activity'

    def __init__(self):
        self.set_key()


recommend_activity_redis = RecommendActivityRedis(day=1, week=12)
# recommend_activity_redis.set_key(day=2)
recommend_all_redis = RecommendAllRedis()
def summd5(str):
    from hashlib import md5
    m = md5()
    m.update(str)
    return m.hexdigest()

if __name__ == "__main__":
    # a = Key()
    # print a['b']['c']

    import base64
    print base64.b64encode(summd5('fdisjvkdslajl'))
    print base64.b64decode('eWlkaWFuOlpWTVJBOG80dnlQQWdITjJtb1lFY3phY1ZhM2lWdGpr')



    print 'Basic',base64.b64encode('douban:ZZFB8nJXNGmfMNiqqUG7XWTXhUhPQa')
    redis = RedisClient.getInstance().redis
    recommend_activity_redis.add('test4', 10000)
    recommend_all_redis.add('test4', 10000)
    # print recommend_all_redis.commit()
    # print recommend_activity_redis.__len__()
    # redis = RedisClient.getInstance().redis
    recommend_activity_redis.add('test5', 10000)
    recommend_all_redis.add('test5', 10010)
    # print recommend_all_redis.commit()
    p = redis.pipeline()
    p.zrange('recommend:activity:1:12', 0, -1, withscores=True)
    p.zrange('recommend:activity:1:10', 0, -1, withscores=True)
    p.zrange('recommend:activity:1:19', 0, -1, withscores=True)
    p.zrange('recommend:all_activity', 0, -1, withscores=True)
    # 11111
    p = redis.pipeline()
    p.zadd('recommend:all_activity', 'test6', '10211')
    p.zrevrange('recommend:all_activity', 0, -1, withscores=False)
    print p.execute()
    a = []
    # redis.sadd('recommend:all_activity:1111', *a)
    # print redis.sismember('free:question_album:items', "103449233214")
    # print result
    # print type(result[0][0][1])


