# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# TODO: 语音切片
# ffmpeg -i 0hxx1.amr -ss 0 -t 50 -ar 8000 -acodec copy lhxx1.amr

import base64

class Config(object):
    #百度语音识别
    BAIDU_ASR_GRANT_TYPE = 'client_credentials'
    BAIDU_ASR_CLIENT_ID = 'Q0tkUc1pmPbkqhHgu7ViBcMl'
    BAIDU_ASR_CLIENT_SECRET = '1dbd8f8419e84377da635e8bd65fec86'


def get_baidu_asr_token():
    import urllib2
    import json

    args = dict(
        grant_type=Config.BAIDU_ASR_GRANT_TYPE,
        client_id=Config.BAIDU_ASR_CLIENT_ID,
        client_secret=Config.BAIDU_ASR_CLIENT_SECRET,
    )
    requrl = ('http://openapi.baidu.com'
              '/oauth/2.0/token'
              '?grant_type=%(grant_type)s'
              '&client_id=%(client_id)s'
              '&client_secret=%(client_secret)s')
    requrl = requrl % args
    response = urllib2.urlopen(requrl)
    resp_str = response.read()
    if resp_str:
        resp_json = json.loads(resp_str)
        token = resp_json.get('access_token', '')
        expiration = resp_json.get('expires_in', 2592000)
        if token:
            return token, expiration
    else:
        print 'baidu asr token update failed'
        return None, None

token, expira = get_baidu_asr_token()
print token

# baidu asr 语音识别接口
# docs: http://yuyin.baidu.com/docs/asr/57

def load_amr_file():
    _f = open('linghun1.amr')
    content = _f.read()
    size = len(content)
    speech = base64.b64encode(content)
    _f.close()
    return size, speech

def baidu_voice2text(token):
    import httplib
    import json
    size ,speech = load_amr_file()
    print size
    requrl = '/server_api'
    header = {
        "Content-Type": "application/json"
    }
    body = {
        'format': 'amr',
        'rate': 8000,
        'channel': 1,
        'cuid': '1231242423re53',
        'token': token,
        "len": size,
        "speech": speech
    }
    body = json.dumps(body)
    conn = httplib.HTTPConnection('vop.baidu.com')
    conn.request(
        method="POST",
        url=requrl,
        body=body,
        headers=header)
    response = conn.getresponse()
    resp_str = response.read()

    if resp_str:
        resp_json = json.loads(resp_str)
        print resp_json
    return resp_json

resp_json = baidu_voice2text(token)

_file = open('result.txt', "a")
if resp_json.get('err_msg') == 'success.':
    print resp_json.get('result')[0]
    _file.write(resp_json.get('result')[0].encode('utf8'))
_file.close()