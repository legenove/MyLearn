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
key = 'ta4E/aspLA3lgFGKmNDNRYU92RkZ4w2t'
def prepare_des_key(key):
    key = base64.decodestring(key)
    return key

key = prepare_des_key(key)

DES_IV = (chr(2)+ chr(8))* 4

BS = DES3.block_size
print BS


def pad1(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def pad2(s):
    pad = BS - len(s) % BS
    return s + chr(pad)*pad
#
# unpad = lambda s : s[0:-ord(s[-1])]


# def pad(data):
#     e = len(data)
#     source = bytearray(data)
#     x = (e + 4) % 8
#     y = 0 if x == 0 else 8 - x
#     sizeByte = bytearray(e)
#     print sizeByte
#     resultByte = range(4 + e + y)
#     resultByte[0:4] = sizeByte[]
#     print resultByte
#     resultByte[4:4 + e] = source
#     for i in range(0, y):
#         resultByte[e + 4 + i] = b"\x00"
#     print resultByte
#     resultstr = ''.join([r for r in resultByte])
#     return resultstr

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
    print resultstr
    return resultstr

def unpad(data):

    resultByte = range(4)
    resultByte[0:4] = data[0:4]

    # 有效数据长度


def http_post(url, jdata):
    r = requests.post(url, data=jdata)      # 发送页面请求
    return r.text


def encrypt3Des(plaintext):
    """
    des3加密

        这里要注意des3的MODE_ecb
    """
    cipher = DES3.new(key, DES3.MODE_ECB)
    msg = cipher.encrypt(pad(plaintext))
    print msg.encode('hex_codec')
    return msg.encode('hex_codec')


def decrypt3Des(plaintext):
    """des4解密"""
    cipher = DES3.new(key, DES3.MODE_ECB)
    msg = cipher.decrypt(plaintext.decode('hex_codec'))
    return msg[4:]

if __name__ == "__main__":

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
