# -*- coding: utf-8 -*-

'''
DB code sample

from tornado.options import define, options
import tornadoasyncmemcache
import redis
from sqlalchemy import create_engine
from sqlalchemy import text

define("db_addr_list", type=list, default=['192.168.0.176:19803'])
define("redis_ip", type=str, default='192.168.1.96')
define("redis_port", type=int, default=19821)
define("mysqldb_engine", type=str,
        default='mysql://root:ktep@192.168.0.27:3306/KTEP')

class MemcachedClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                tornadoasyncmemcache.ClientPool(options.db_addr_list,
                                                maxclients=100)
        return cls._instance

class RedisClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                redis.StrictRedis(host=options.redis_ip,
                                    port=options.redis_port, 
                                    db=0)
        return cls._instance

class MySQLClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                    create_engine(options.mysqldb_engine, echo=True)
        return cls._instance

def get_memcached(key, callback):
    MemcachedClient().get(key, callback=callback)

def get_redis(key):
    RedisClient().get(key)

def set_redis(key, value):
    RedisClient().set(key, value)

def get_mysql(param):
    sql="select * from table_name where param=:param";
    result = MySQLClient().execute(text(sql), {'param':param}).fetchall()
    return result
'''

import os
from os import getenv
import psycopg2
import traceback
from tornado.options import define, options

define("db_host", type=str, default=getenv('DB_HOST',''))
define("db_port", type=int, default=getenv('DB_PORT',''))
define("db_user", type=str, default=getenv('DB_USER',''))
define("db_password", type=str, default=getenv('DB_PASSWORD',''))
define("db_database", type=str, default=getenv('DB_DATABASE',''))


class Database(object):
    def __init__(self, *args, **kwargs):
        self.conn = None

    def _connect(self):
        raise NotImplementedError

    def _close(self):
        raise NotImplementedError

    def _reconnect(self):
        self.close()
        self.connect()

    def query(self, sql):
        raise NotImplementedError

    def update(self, sql):
        raise NotImplementedError


class PostgreSQL(Database):
    def __init__(self, *args, **kwargs):
        super(PostgreSQL, self).__init__(*args, **kwargs)
        self.dbtype = 'postgresql'

    def _connect(self):
        try:
            if type(options.db_port) != int:
                options.db_port = int(options.db_port)
            self.conn = psycopg2.connect(
                host=options.db_host,
                user=options.db_user,
                password=options.db_password,
                database=options.db_database,
                port=options.db_port,
            )
            self.conn.autocommit = True
            #self.conn.set_client_encoding('utf8')
        except psycopg2.Error as e:
            print traceback.format_exc()
            print 'connect error: {0} - "{1}"'.format(e.pgcode, e.pgerror)

        return True if self.conn else False

    def _close(self):
        try:
            if self.conn:
                self.conn.close()
        except psycopg2.Error as e:
            print traceback.format_exc()
            print 'close error: {0} - "{1}"'.format(e.pgcode, e.pgerror)
        finally:
            self.conn = None

    def query(self, sql):
        ret = False
        rows = []
        try:
            self._connect()
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            ret = True
        except psycopg2.Error as e:
            print traceback.format_exc()
            print 'query error: {0} - "{1}"'.format(e.pgcode, e.pgerror)
        finally:
            self._close()
        return ret, rows

    def update(self, sql):
        ret = False
        try:
            self._connect()
            cur = self.conn.cursor()
            cur.execute(sql)
            ret = True
        except psycopg2.Error as e:
            print traceback.format_exc()
            print 'query error: {0} - "{1}"'.format(e.pgcode, e.pgerror)
        finally:
            self._close()
        return ret
