# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import httplib
import urllib, urllib2
import json
import logging
from xml.dom.minidom import parseString
import time
import random
import gzip
import requests
from io import BytesIO

def gzip_decode(data):
    import StringIO, gzip
    try:
        compressed_stream = StringIO.StringIO(data)
        gziper = gzip.GzipFile(fileobj=compressed_stream)
        data2 = gziper.read()
        return data2
    except Exception, e:
        logging.error(e)
        return data

def real_result(request_header, response, data):
    encode_type = response.getheader("content-encoding")
    if encode_type and "gzip" == encode_type.lower():
        return gzip_decode(data)
    else:
        encode_type = response.getheader("Content-Encoding")
        if encode_type and "gzip" == encode_type.lower():
            return gzip_decode(data)
        else:
            return data


class BaseRequestApi(object):

    TimeOut = 3
    DEBUG_LEVEL = 1
    HOST = ""

    @classmethod
    def request(cls, method, path, params, headers={}):
        host = cls.HOST
        _headers = {'Accept-Language': 'zh-cn', 'User-Agent': 'Python/Automate', "Accept-Charset": "utf-8"}
        _headers.update(headers)

        conn = httplib.HTTPConnection(host, timeout=cls.TimeOut)

        for k, v in params.items():
            if v == '' or v == None:
                del params[k]

        params = urllib.urlencode(params)
        if method == "GET":
            path = "%s?%s" % (path, params)
            params = ''
        else:
            path = "%s" % path

        logging.debug("*[Requst]* %s %s %s" % (method, host + path, params))
        conn.request(method, path, params, _headers)
        #conn.set_debuglevel(cls.DEBUG_LEVEL)
        try:
            r = conn.getresponse()
            return r
        except Exception,e:
            logging.error("*[Requst]* %s %s %s request error:%s" % (method, host + path, params,e))
            raise e
        finally:
            conn.close()


    @classmethod
    def post_body_request(cls, path, body, headers={}):
        host = cls.HOST
        method = "POST"

        _headers = {'Accept-Language': 'zh-cn', 'User-Agent': 'Python/Automate', "Accept-Charset": "utf-8"}
        _headers.update(headers)

        conn = httplib.HTTPConnection(host, timeout=cls.TimeOut)
        path = "%s" % path

        logging.debug("*[Requst]* %s %s %s" % (method, host + path, body))

        conn.request(method, path, body, _headers)
        #conn.set_debuglevel(cls.DEBUG_LEVEL)
        try:
            r = conn.getresponse()
            return r
        except Exception,e:
            logging.error("*[Requst]* %s %s %s request error:%s" % (method, host + path, body,e))
            raise e
        finally:
            conn.close()

    @classmethod
    def get(cls, path, params, headers={}):
        return cls.request("GET", path, params, headers)

    @classmethod
    def get_data(cls, path, params, headers={}):
        return cls.request("GET", path, params, headers).read()

    @classmethod
    def get_json(cls, path, params, headers={}):
        return json.loads(cls.request("GET", path, params, headers).read())

    @classmethod
    def post(cls, path, params, headers={}):
        return cls.request("POST", path, params, headers)

    @classmethod
    def post_data(cls, path, params, headers={}):
        return cls.request("POST", path, params, headers).read()

    @classmethod
    def post_json(cls, path, params, headers={}):
        return json.loads(cls.request("POST", path, params, headers).read())

