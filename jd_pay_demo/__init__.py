# -*- coding: utf-8 -*-
"""
京东接口
"""

import json
import base64
import requests
import struct
import xmltodict
import hashlib
from dicttoxml import dicttoxml

from urllib import urlencode

from M2Crypto import RSA
from Crypto.Hash import SHA256 as SHA
from Crypto.Cipher import DES3

from xml.dom.minidom import Document, parseString as xml_parse_string

TIMEOUT = 2


def create_key(sk):
    key = base64.decodestring(sk)
    return key


def add_xml_node(root, k, v):
    doc = Document()
    node = doc.createElement(k)
    text = doc.createTextNode(str(v))
    node.appendChild(text)
    root.appendChild(node)


def prepare_xml(params):
    result = {
        'version': params['version'],
        'merchant': params['merchant']
    }
    cp_params = params.copy()
    xml_res = dicttoxml(cp_params, attr_type=False, custom_root='jdpay')
    sign = build_mysign(xml_res)
    end = xml_res.find('</jdpay>')
    xml_res = xml_res[:end] + '<sign>' + str(sign) + '</sign>' + xml_res[end:]
    result.update(
        encrypt=base64.standard_b64encode(encode_des(smart_str(xml_res))))
    return dicttoxml(result, attr_type=False, custom_root='jdpay')


def params_filter(params, delimiter='&', charset='utf-8', excludes=['sign'],
                  excludes_des=['merchant', 'version', 'sign'], des=True):
    ks = params.keys()
    ks.sort()
    newparams = {}
    prestr = ''
    if params.get('_input_charset', None):
        charset = params['_input_charset']
    for k in ks:
        v = params[k]
        k = smart_str(k, charset)
        if k not in excludes and v != '':
            if isinstance(v, dict):
                v = json.dumps(v, sort_keys=True, separators=(',', ':'))
            else:
                v = smart_str(v, charset)
            newparams[k] = encode_des(v) if des and k not in excludes_des else v
            prestr += '%s=%s%s' % (k, v, delimiter)
    prestr = prestr[:-1]
    return newparams, prestr


# 生成签名结果
def build_mysign(prestr):
    key = RSA.load_key(Config.JDPAY_PRIVATE_KEY)
    signature = key.private_encrypt(SHA.new(prestr).hexdigest(), RSA.pkcs1_padding)
    # base64 编码，转换为unicode表示并移除回车
    sign = base64.encodestring(signature).decode("utf8").replace("\n", "")
    return sign

def verify_mysign(sign, xml_str):
    xml_sha_str = SHA.new(xml_str).hexdigest()
    key = RSA.load_pub_key(Config.JDPAY_PUBLIC_KEY)
    signature = key.public_decrypt(base64.standard_b64decode(sign),
                                   RSA.pkcs1_padding)
    return signature == xml_sha_str

def des_pad(data):
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

def un_des_pad(data):
    resultByte = data[0:4]
    e = struct.unpack('>I', resultByte)[0]
    x = (e + 4) % 8
    y = 0 if x == 0 else 8 - x
    return data[4:] if y == 0 else data[4:-y]

def encode_des(param):
    key = create_key(Config.JDPAY_MERCHANT_DESKEY)
    des3 = DES3.new(key, DES3.MODE_ECB)
    param = des3.encrypt(des_pad(param)).encode('hex_codec')
    return param


def decode_des(param):
    key = create_key(Config.JDPAY_MERCHANT_DESKEY)
    des3 = DES3.new(key, DES3.MODE_ECB)
    param = param.decode('hex_codec')
    param = des3.decrypt(param)
    return un_des_pad(param)


class JDpay(object):
    '''
    手机网站支付
    ALIPAY_GATEWAY:https://h5pay.jd.com/jdpay/saveOrder
    H5: https://h5pay.jd.com/jdpay/saveOrder
    '''

    GATEWAY = Config.JDPAY_GATEWAY

    def get_base_params(self):
        params = dict(
            version='V2.0',
            merchant=Config.JDPAY_MERCHANT_NUM,
        )
        return params

    def prepare_url(self, params):
        _params = self.get_base_params()
        params.update(_params)
        newparams, prestr = params_filter(params)
        sign = build_mysign(prestr)
        newparams['sign'] = sign
        prestr = urlencode(newparams)
        url = self._full_url(prestr)
        return url

    def _full_url(self, prestr):
        return '%s%s' % (self.GATEWAY, prestr)

    def make_request(self, method, url, **kwargs):
        try:
            req = requests.request(method, url, timeout=TIMEOUT, **kwargs)
            req.raise_for_status()
        except requests.RequestException as e:
            pass
        else:
            result = req.text
            result = self.verify_result(result)
            if result:
                return result
        return {}

    def verify_result(self, result):
        res = xmltodict.parse(result, encoding='UTF-8')
        code = res['jdpay']['result']['code']
        if code != '000000':
            return None
        encrypt = res['jdpay']['encrypt']
        return decode_des(base64.standard_b64decode(encrypt))


def notify_verify(xml_data):
    xml_str = decode_des(base64.standard_b64decode(xml_data))
    sign_begin = xml_str.find('<sign>')
    sign_end = xml_str.find('</sign>')
    if sign_begin>0 and sign_end>0:
        sign = xml_str[sign_begin+6:sign_end]
        xml_new_str = xml_str[:sign_begin] + xml_str[sign_end+7:]
        if verify_mysign(sign, xml_new_str):
            return xml_new_str
    return False




