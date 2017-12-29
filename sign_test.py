# -*- coding: utf-8 -*-

import pytz

from hashlib import md5
import time, datetime


def params_filter(params, delimiter='&', charset='utf-8',
                  excludes=['sign', 'sign_type']):
    ks = params.keys()
    ks.sort()
    newparams = {}
    prestr = ''
    for k in ks:
        v = params[k]
        if k not in excludes and v != '':
            prestr += b'%s=%s%s' % (k, params[k], delimiter)
    prestr = prestr[:-1]
    return newparams, prestr


def build_sign(prestr, sign_type='MD5'):
    key = 'OWUwNzI1ODEyMmFmMjI5YzlhYmY1ZTY5'  # SECRET KEY
    print prestr
    if sign_type == 'MD5':
        prestr += '&key=%s' % str(key)
        return md5(prestr).hexdigest().lower()
    return ''


a = [{u'main_card_question_id': u'90000034295715129720',
      u'main_card_active': True,
      u'main_card_short_title': u'\u653e\u725b\u5a03\u73ef\u7fa9\u4f60\u653e\u5047\u4e86\u53bb\u54ea\u7236\u8001\uff1b\u4e0a\u653e\u7a7a\u6c14\uff1b\u5965\u514b\u65af\u5361\u4f5b\u554a\u963f\u4f5b\uff1b\u6316\u8033\u52fa\u7684\u9ebb\u70e6\u9a82\u6211\uff1b\u6536\u5230\u9a6c\u4e0a\u653e\u91cc\u9762\u672a\u6536\u5230\u514d\u8d39\u665a\u4e0a\u7684',
      u'main_card_albums_id': u'1034295091726158',
      u'main_card_answer_nickname': u'\u963f\u5973\u8bf4\u4e0b\u6b21\u5973\u665a\u793c\u670d\u662f\u5185\u5b58\u5361\u4e24\u4f4d\u6570\u7684\u5976\u7c89\u9ebb\u70e6\uff1b\u53d1\u9ebb\u70e6\u4f20\u5a92\u7f51\uff1b\u7231\u4e0a\u65b9\u9762\uff1b\u554a\u6c99\u53d1\u51ef\u6492\u7684\u5f00\u53d1\u4e86\u65b0\u5e74\uff1b\u7231\u4e0a\u5c31\u6253\u5f00\uff1boasis\u90a3\u5f97\u770b\u7236\u6bcd\u9648\u6587\u79d1\u751f\u7684'},
     {u'main_card_question_id': u'90000034295715129720',
      u'main_card_active': True,
      u'main_card_short_title': u'\u95ee\u9898\u77ed\u6807\u9898\u54c8\u54c8\u54c8\u54c8\u6700\u591a15\u4e2a\u5b57 \u80fd\u663e\u793a\u51e0\u4e2a\u5462\u54c8\u54c8\u54c8\u54c8\u54c8\u54c8',
      u'main_card_albums_id': u'1034295091726158',
      u'main_card_answer_nickname': u'\u7b54\u4e3b\u6635\u79f0\u4f60\u53d1\u8985\u5783\u573e\u6b7b\u591a\u5c11\u6b21\u7684\u8303\u6316\u6398\u7684\u4f5b\u724c\u6211\u5f1f\u8bf4'}]


def build_params():
    params = {
        "username": "123",
        "password": "123",
        "auth_approach": "douban",
        "grant_type": "password"
    }
    from dateutil import parser

    date = parser.parse('2016-12-08T09:39:23.502947+00:00')
    print date
    params['timestamp'] = int(time.mktime(date.timetuple()))
    print params['timestamp']
    return params


def sign(method, args, json):
    params = build_params()
    _, prestr = params_filter(params)
    sign = build_sign(prestr)
    return sign


# print sign(None, None, None)


# --header 'Authorization: Basic ZG91YmFuOlpaRkI4bkpYTkdtZk1OaXFxVUc3WFdUWGhVaFBRYQ=='
# --header 'Sign: 0bdb0410134b62bd8f1c1d80b6b5ed7f'
# --header 'Date: 2016-12-08T09:39:23.502947+00:00'

import hashlib
from Crypto.Cipher import DES3,DES
import base64


def create_key(sk):
    r = hashlib.md5(sk).digest()
    return r + r[:8]


def init_str(s):
    l = len(s) % 16
    if l != 0:
        c = 16 - l
        s += chr(c) * c
    return s


key = '2345'  # 秘钥
b2bpwd = "oohbvdlkfjdslakfjlksdalskckdl"
ss = init_str(b2bpwd)

def encode_des(param):
    key = 'jdkeyoficmdkfdxddfscdvds' # Config.JDPAY_DES_KEY
    des3 = DES.new(key, DES3.MODE_ECB)
    param = des3.encrypt(init_str(param))
    param = base64.standard_b64encode(param)
    return param


def decode_des(param):
    key = 'ta4E/aspLA3lgFGKmNDNRYU92RkZ4w2t' # Config.JDPAY_DES_KEY
    des3 = DES3.new(key, DES3.MODE_ECB)
    param = base64.standard_b64decode(param)
    param = des3.decrypt(param)
    return param
# b2 = encode_des(ss)
# print b2
# b22 = decode_des(b2)
# print ss
# print b22
# print b2bpwd

params = dict(
            version='V2.0',
            merchant='1231242',
            currency='CNY',
        )
from xml.dom.minidom import Document, parseString as xml_pars_string
import xmltodict

def add_xml_node(root, k, v):
    doc = Document()
    node = doc.createElement(k)
    text = doc.createTextNode(v)
    node.appendChild(text)
    root.appendChild(node)

def prepare_xml(params, charset='UTF-8',
                excludes=['merchant', 'verion']):
    new_xml = Document()
    pre_xml = Document()
    root = new_xml.createElement('jdpay')
    new_xml.appendChild(root)
    prexml_root = pre_xml.createElement('jdpay')
    pre_xml.appendChild(prexml_root)
    for exclude in excludes:
        if exclude in params:
            v = params.pop(exclude)
            add_xml_node(root, exclude, v)
            add_xml_node(prexml_root, exclude, v)
    for k, v in params.iteritems():
        add_xml_node(prexml_root, k, v)
    parstr = pre_xml.toxml(encoding=charset)
    add_xml_node(prexml_root, 'sign', build_mysign(parstr))
    add_xml_node(root, 'encrypt',
                 encode_des(pre_xml.toxml(encoding=charset)))
    return new_xml.toprettyxml(encoding=charset)

def build_mysign(prestr):
    sign = base64.encodestring(prestr).decode("utf8").replace("\n", "")
    return sign

xmlstr = '''<?xml version="1.0" encoding="utf-8"?>
<jdpay>
  <version>V2.0</version>
  <merchant>22294531</merchant>
  <result>
    <code>000000</code>
    <desc>成功</desc>
  </result>
  <encrypt>N2ZjNmIwMzJiMjA5ZTNhZDhjNjc0YmY1ZWJlY2QyODU0YTc5NmQ3ZWQxMWU1NzE3MWQ0OTUwOGI5NzllYmE4ZjM1YzRiZjlmYWE1M2ZiYjVjYTg5YjA4NTdhMjg3NTBhNzQxM2ZjOWFlN2U3YTNlYzM5ZTI5OTBkZDczNzQ5MjhjM2UxMjhkYWJhMGM0NWY2MWFjYjg2YWFlZDBjOTQ1Y2UyOWNlMDg2MmViOTQ3ZDUyZTczOTMxYjM0NGQwZTNjZGVjZTNkY2EwZmZlYzZlODE1Njc3YWMzODcyNTRhYTcyZDc5MjNhYzc5YWIzZGM0ZGIwYWE4NTc3ZTRhNmE3YmMxMjIwMmEyZmRjMDgxNjhlZjQ5ODVlNGIwNmU2ZTVjZjk3MWRlMmQ5NWYxMmJjNjFiOTY3M2E1ZGY0NWVkNmQ5NzU4OTFmNjFjNTMxMjQ0ZTUyZTdhOWZjNGYwYWRiNTM0ZTQyNGEzMWQyZTYyMWFkMWZkNWY2YTZkZDFmOWNkMTljODg2MzkxNmYwMWViNWMzM2JhNTM5ZWMxYjY1NTA2ZTdmMTYzMjY2YTVjZTk1OTE5M2U0NzNhMGNhMWIwMmVhZjdmYzUyYjc3ZDRiM2Y2NDVlNDFjMDI2YTM0YjU0MGE5MDQzZDEyYmRjNzQzYzM5ODc5NTRhMDcyNGFiOTI4NWQ3MmE0OWUwODNlNGZlNmM3OGMxNGJiNDAzMzI5YTVlMWViNjM2Y2ZkYTg5ZTc1ZDk2ZmJjNTcwMTIyYjU3NWUxZWI2MzZjZmRhODllNzFkYTM0NTE0MDM3YmU5ODQzZTI3Y2Y5OGFjYWM5ZGI3YTg4Yjk5YTQ5NjAxNWYyOWQxZjYwNTJmM2JhOWFlMWI0MzY2Yzc4MmY5YzJlNDY3ODljZjc3ZDMzYjVkN2IyZWRlZjcyOGQ0N2ViZDJkN2Y1YTA5ZTJiYTk5NjUxMGZjNmExMTA3OTFjMjY0NTMyODQ3YjRiYjc3MDlkMmY4YzllY2ZlNzE2MTE1ZjNkMzRlZGRhMmFhOGU4NTA0NThiZTdiOWUzYTM0MDczZTFjNzgxZDFkYzY1ZTRjYzRiYTY3ZGE4NzE4ZjJjNDBmMGU5ZDZlNWU2Y2RiNzAyMzUyNDIyZGVkYmU4NWM4MDdlZTVkNDhkZjg0NGMwNGUwMzA1ZWM5ODJkNmIwMWRmMzg3MjZjZGRkMTVhMWI4YjI1YTdhMWVmNTI2MDUzYmYzYzFlYTBmYmM2MTI3MDMwNTcyNTU1MzQyYjA0ZmZjN2NjOTg4Y2Q2YjQ1M2JhMDQ1NmE3ODUzNDMzMmNmNDFiNWI0M2M5ODhmNmNkMDI2MjFlZDIwYzRhYjliMjU2YmM3ZDU1Yzg2OTBkZWZjNTVhYjA1NzdiYzQxZmY0MzAxNmE3OTRlNWVkMjRjNDc4ZDgzN2JhNDZhMDAwY2ExOGMwMDQ4MWEwMmUyZTcyZjIwYTE0N2MyMTUwMWI3Mjg0NWE0ZDY3YTFiYTEyYzI2MTljYzhkMGM5YzJhOWU1NDljYmY0ZDJlYTM5M2IxYTg5ZWQ4NjMxZWM4NmIwNDI0YzJkYzBjNDU=</encrypt>
</jdpay>
'''
xmlstr = '''<?xml version="1.0" encoding="UTF-8"?>
<jdpay>
<version>V2.0</version>
<merchant>22310318</merchant>
<result>
	<code>000000</code>
	<desc>success</desc>
</result>
<device>12345</device>
<tradeNum>123456789</tradeNum>
<tradeType>0</tradeType>
<sign>19f9ce32be414ef8219f9ce32be414ef82b84a9079493b71a9079493b71a</sign>
<note>test</note>
<amount>100</amount>
<status>0</status>
<payList>
	<pay>
		<payType>0</payType>
		<amount>100</amount>
		<currency>CNY</currency>
		<tradeTime>20160101103015</tradeTime>
		<detail>
			<cardHolderName>*小白</cardHolderName>
			<cardHolderMobile>138****1234</cardHolderMobile>
			<cardHolderType>0</cardHolderType>
			<cardHolderId>****0001</cardHolderId>
			<cardNo>6012345****6789</cardNo>
			<bankCode>ICBC</bankCode>
			<cardType>1</cardType>
</detail>
	</pay>
</payList>
</jdpay>
'''

# xmlstr = '''<?xml version="1.0" encoding="UTF-8"?>
# <jdpay>
# <version>V2.0</version>
# <merchant>22294531</merchant>
# <result>
# <code>000000</code>
# <desc>成功</desc>
# </result>
# <orderId>1029148637575787617463</orderId>
# <merchantName>京东支付测试商户号</merchantName>
# <amount>1</amount>
# <expireTime>600</expireTime>
# <tradeNum>1486346954111</tradeNum>
# <qrCode>https://h5pay.jd.com/code?c=616zlks7djfb1z</qrCode>
# <sign>C5Mn72q+w1ttkqsUSuhFwJjK8rpikxHkPHaJAXNBVvJGOLMYrSRkHTchACkAISiUzJ60ppWC4DnN6nfnbT5xyrK7kKmHuUivfGRGVnfucvZnV7eDS0Jv+7Np64P/ZyHUkesTDxb0+oDNilTaX82pV5Y2O0qmfs5Ft0LhpJ4Le/w=</sign>
# </jdpay>
# '''

# import json
# # doc = xmltodict.parse(xmlstr, encoding='UTF-8')
# # doc_json = json.dumps(doc)
# # print json.dumps(xmltodict.parse(xmlstr).get('jdpay'))
# # print doc_json
# # print doc['jdpay']['result']['code']
#
# doc = xml_pars_string(xmlstr)
# # root = doc.documentElement
# sign_node = doc.getElementsByTagName("sign")[0]
# sign = sign_node.childNodes[0].nodeValue
# doc.documentElement.removeChild(sign_node)
# print doc.toxml(encoding='UTF-8')
#
# print json.dumps(xmltodict.parse(xmlstr).get('jdpay'))


# -*- encoding:utf-8 -*-
import base64
import re
import struct

import requests
import xmltodict
from Crypto.Cipher import DES3

"""
* 将元数据进行补位后进行3DES加密
* <p/>
* 补位后 byte[] = 描述有效数据长度(int)的byte[]+原始数据byte[]+补位byte[]
*
* @param
*            sourceData 元数据字符串
* @return 返回3DES加密后的16进制表示的字符串
*/
"""
"""
1.DES3加密模式
2.补位方式
3.#0,0x00,'0','\x00'的区别

"""
key = base64.decodestring('ta4E/aspLA3lgFGKmNDNRYU92RkZ4w2t')

DES_IV = "11111111"

BS = DES3.block_size


def pad1(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#
# unpad = lambda s : s[0:-ord(s[-1])]


def pad(data):
    e = len(data)
    x = (e + 4) % 8
    y = 0 if x == 0 else 8 - x
    sizeByte = struct.pack('>I', e)
    resultByte = range(len(sizeByte) + e + y)
    resultByte[0:4] = sizeByte
    resultByte[4:4 + e] = data
    for i in range(0, y):
        resultByte[e + 4 + i] = "\x00"
    resultstr = ''.join(resultByte)
    return resultstr


def unpad(data):

    resultByte = range(4)
    resultByte[0:4] = data[0:4]
    data = ''.join([s for s in data if s != "\x00"])

    # 有效数据长度


def http_post(url, jdata):
    r = requests.post(url, data=jdata)      # 发送页面请求
    return r.text


def encrypt3Des(plaintext):
    """
    des3加密

        这里要注意des3的MODE_
    """
    cipher = DES3.new(key, DES3.MODE_ECB)
    msg = cipher.encrypt(pad(plaintext))
    return msg.encode('hex_codec')


def decrypt3Des(plaintext):
    """des4解密"""
    cipher = DES3.new(key, DES3.MODE_ECB)
    msg = cipher.decrypt(plaintext.decode('hex_codec'))
    return msg[4:]

if __name__ == "__main__":

    #     b = struct.pack('>I',3)
    #     print b
    print pad("111")

    print pad1("111")
#
    print "加密"
    plaint_test = "0035641771382207Q589547180E58417"
    print len(plaint_test)
    a = encrypt3Des(plaint_test)
    print base64.encodestring(a).replace('\n', "")
    a = base64.decodestring('NzYzYmZkNDRlMTk2MzA2M2RlMDQ1N2M0NmU5YWFmZDJmNTVmZWYwNTZiY2I3YjFhYWM5NmNjMzUxNzAyYjhiYWM5ZjIwNzZiZjgyNzY0ZTA=')
    b = decrypt3Des(a)

    print len(b)
    print b
#     print "解密"
