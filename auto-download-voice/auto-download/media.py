# -*- coding: utf-8 -*-
import string
import random
from urlparse import urlparse

import requests
from requests.exceptions import ConnectTimeout, ReadTimeout

from flask import current_app as app
from qiniu import Auth, PersistentFop, op_save, BucketManager

from settings import Config
from zaih_core.ztime import now
from datetime import timedelta


def generate_nonce_str(length=32):
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(length))


def get_qiniu_file_avinfo(url):
    try:
        req = requests.get(url)
    except (ConnectTimeout, ReadTimeout):
        return {}
    if req.status_code == 200:
        info = req.json()
        return info.get('format', {})
    return {}


def get_qiniu_file_duration(url):
    '''七牛私有空间音频资源avinfo中duration'''
    info = get_qiniu_file_avinfo(url)
    if not info:
        return None
    duration = info.get('duration', 0)
    try:
        duration = int(float(duration) + 0.5)
        return duration
    except ValueError:
        return None


def get_qiniu_file_size(url):
    '''七牛私有空间音频资源avinfo中duration'''
    info = get_qiniu_file_avinfo(url)
    if not info:
        return None
    size = info.get('size', 0)
    try:
        size = int(size) / 1000
        return size
    except ValueError:
        return None


def get_qiniu_file_md5(url):
    try:
        req = requests.get(url)
    except (ConnectTimeout, ReadTimeout):
        return ''
    if req.status_code == 200:
        info = req.json()
        return info.get('md5', '')
    return ''


def qiniu_private_url_gen(key, avinfo=False, md5=False, expires=1800):
    '''七牛私有空间资源下载链接生成器'''
    q = qiniu_auth()
    bucket_host = Config.QINIU_PRIVITE_HOST
    base_url = '%s/%s' % (bucket_host, key)
    if avinfo:
        base_url = '%s/%s?avinfo' % (bucket_host, key)
    elif md5:
        base_url = '%s/%s?hash/md5' % (bucket_host, key)
    return q.private_download_url(base_url)


def qiniu_private_avinfo_duration(key):
    '''七牛私有空间音频资源avinfo中duration'''
    private_url = qiniu_private_url_gen(key, avinfo=True)
    duration = get_qiniu_file_duration(private_url)
    return duration


def qiniu_private_avinfo_size(key):
    '''七牛私有空间音频资源avinfo中duration'''
    private_url = qiniu_private_url_gen(key, avinfo=True)
    size = get_qiniu_file_size(private_url)
    return size


def qiniu_private_file_md5(key):
    private_url = qiniu_private_url_gen(key, md5=True)
    req = requests.get(private_url)
    if req.status_code == 200:
        info = req.json()
        return info.get('md5', '')
    return ''


def media_for(hash, scheme=None, style=None):
    if not hash:
        return None
    url = hash.split('!')[0]
    up = urlparse(url)
    hash_domain = up.hostname
    if hash_domain and hash_domain not in Config.QINIU_DOMAINS:
        return hash
    _hash = up.path
    if len(_hash) != 0 and _hash[0] == '/':
        _hash = _hash[1:]

    media_host = Config.QINIU_HOST
    url = '%s/%s' % (media_host, _hash)
    if url.endswith('.amr'):
        url = '%s.mp3' % url[:-4]
    if url and style:
        url = '%s!%s' % (url, style)
    return url


def image_for(image, style=None, scheme=None):
    url = media_for(image, scheme=scheme, style=style)
    return url


def get_weixin_media_url(media_id):
    from settings import Config
    from services.wxconfig import get_weixinmp_token
    appid = Config.WEIXINMP_APPID
    url = 'http://file.api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s'
    access_token, errors = get_weixinmp_token(appid)
    if errors:
        # TODO 提交到sentry
        return
    media_url = url % (access_token, media_id)
    return media_url


def media_fetch(media_id):
    '''抓取url的资源存储在私有库'''
    media_url = get_weixin_media_url(media_id)
    if media_url:
        auth = qiniu_auth()
        bucket = BucketManager(auth)
        bucket_name = Config.QINIU_PRIVITE_BUCKET
        fetch_key = '%s%s.amr' % (media_id, random.randint(1, 1000))
        ret, info = bucket.fetch(media_url, bucket_name, fetch_key)
        if info.status_code == 200:
            # media_saves 转码
            saveas_key = media_saveas(fetch_key)
            if saveas_key:
                return saveas_key
            return fetch_key


def get_media_duration(voice_url):
    """
    :params voice_url: qiniu voice key
    """
    media_url = media_for(voice_url)
    if not media_url:
        return None
    media_url = '%s?avinfo' % media_url
    duration = get_qiniu_file_duration(media_url)
    return duration


def get_media_size(voice_url):
    """
    :params voice_url: qiniu voice key
    """
    media_url = media_for(voice_url)
    if not media_url:
        return None
    media_url = '%s?avinfo' % media_url
    size = get_qiniu_file_size(media_url)
    return size


def get_media_md5(voice_url):
    media_url = media_for(voice_url)
    if not media_url:
        return None
    media_url = '%s?hash/md5' % media_url
    md5 = get_qiniu_file_md5(media_url)
    return md5



def qiniu_auth():
    access_key = str(Config.QINIU_ACCESS_TOKEN)
    secret_key = str(Config.QINIU_SECRET_TOKEN)
    auth = Auth(access_key, secret_key)
    return auth


def media_saveas(key):
    '''多媒体持久化
       逻辑是：首先去确认私有库中存在key，没有
               则去公有库找，找到就copy一份到私有库，
               公有库也不存在就忽视
    '''
    auth = qiniu_auth()
    bucket = BucketManager(auth)
    private_bucket_name = Config.QINIU_PRIVITE_BUCKET
    public_bucket_name = Config.QINIU_PUBLIC_BUCKET
    ret, info = bucket.stat(private_bucket_name, key)
    if not ret:
        ret, info = bucket.stat(public_bucket_name, key)
        if ret:
            ret, info = bucket.copy(public_bucket_name, key,
                                    private_bucket_name, key)
    # 转码是使用的队列名称。
    pipeline = 'zaih_media'
    # 要进行转码的转码操作。
    fops = "avthumb/mp3/ab/192k/ar/44100/acodec/libmp3lame"
    # 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
    saveas_key = "%s.mp3" % key.split('.')[0]
    fops = op_save(fops, private_bucket_name, saveas_key)
    pfop = PersistentFop(auth, private_bucket_name,
                         pipeline, Config.QINIU_NOTIFY_URL)
    ret, info = pfop.execute(key, [fops], 1)
    if ret is not None:
        return saveas_key


def media_saveas_amr(from_key, to_key):
    auth = qiniu_auth()
    pipeline = 'zaih_media'
    fops = "avthumb/amr/ab/128k/ar/8000"
    saveas_key = to_key
    private_bucket_name = Config.QINIU_PRIVITE_BUCKET
    fops = op_save(fops, private_bucket_name, saveas_key)
    pfop = PersistentFop(auth, private_bucket_name, pipeline,
                         Config.QINIU_FILTER_NOTIFY_URL)
    ops = []
    ops.append(fops)
    ret, info = pfop.execute(from_key, ops, 1)
    # print info
    if ret is not None:
        return saveas_key


def voice_to_text_sync():
    import base64
    import httplib
    import json
    file_data = open('/app/zzhifubao/90000032837000800243aa.1.amr', 'rb')
    voice_data = file_data.read()
    voice_data64 = base64.b64encode(voice_data)
    file_data.close()

    requrl = '/server_api'
    header = {
        "Content-Type": "application/json"
    }
    body = {
        'format': 'amr',
        'rate': 8000,
        'channel': 1,
        'cuid': '02:42:10:e3:48:94',
        'token': 'aaaa',  # Config.BAIDU_ASR_TOKEN,
        'speech': voice_data64,
        'len': len(voice_data),
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
    print resp_str
    if resp_str:
        resp_json = json.loads(resp_str)
    if resp_json['err_no'] == 0:
        contents = resp_json['result']
        for content in contents:
            if not check_nigger(content):
                # print content, 'is ok'
                continue
            # print content, 'is suspectable'
        return resp_json
    elif resp_json['err_no'] == 3302:
        update_baidu_asr_token()
    return {}


# baidu asr 语音识别接口
# docs: http://yuyin.baidu.com/docs/asr/57
def voice_to_text(voice_url, question_id, token):
    import httplib
    import json
    requrl = '/server_api'
    header = {
        "Content-Type": "application/json"
    }
    body = {
        'format': 'amr',
        'rate': 8000,
        'channel': 1,
        'cuid': '02:42:10:e3:48:94',
        'token': token,
        'url': voice_url,
        'callback': '%s/%s' % (Config.QINIU_RECOGNITION_NOTIFY_URL, str(question_id))
    }
    # print body
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
    return resp_json


def update_baidu_asr_token():
    import urllib2
    import json
    token = ''
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
            date_expiration = now() + timedelta(seconds=expiration)
            return True, token, date_expiration
    else:
        print 'baidu asr token update failed'
        return False, None, None

def xunfei_voice2text(voice_url, voice_id):
    import base64
    import httplib
    import json

    base_url = Config.XUNFEI_WEBAPI_HOST

    # path parameters
    req_url = Config.XUNFEI_WEBAPI_RECOGNITION_PATH
    req_url += '?svc=%(svc)s&token=%(token)s&auf=%(auf)s'
    req_url += '&aue=%(aue)s&ent=%(ent)s'
    path_params = dict(
        svc='iat',
        token=Config.XUNFEI_WEBAPI_TOKEN,
        auf='audio/L16;rate=8000',
        ent='sms8k',
        aue='amr',
    )
    req_url = req_url % path_params

    # header parameters
    xpar_args = dict(
        imei='1111',
        imsi='1111',
        mac='1111',
        appid=Config.XUNFEI_WEBAPI_APP_ID,
    )
    xpar = 'imei=%(imei)s&imsi=%(imsi)s&mac=%(mac)s&appid=%(appid)s'
    xpar = xpar % xpar_args
    xpar_encode = base64.b64encode(xpar)

    header = {
        "Content-Type" : "text",
        "X-Par": xpar_encode,
    }

    # body parameters
    body = {
        'audio_url': voice_url,
        'callback': '%s/%s' % (Config.XUNFEI_WEBAPI_RECOGNITION_NOTIFY_URL,
                               str(voice_id))
    }
    body = json.dumps(body)
    body = base64.b64encode(body)

    conn = httplib.HTTPConnection(base_url)
    conn.request(
        method="POST",
        url=req_url,
        body=body,
        headers=header)
    response = conn.getresponse()
    resp_str = response.read()

    resp_json = {'err_no': -1}
    if resp_str:
        resp_json['err_no'] = 0
        resp_json['ret'] = resp_str
    return resp_json

