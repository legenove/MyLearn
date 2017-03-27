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


print sign(None, None, None)


# --header 'Authorization: Basic ZG91YmFuOlpaRkI4bkpYTkdtZk1OaXFxVUc3WFdUWGhVaFBRYQ=='
# --header 'Sign: 0bdb0410134b62bd8f1c1d80b6b5ed7f'
# --header 'Date: 2016-12-08T09:39:23.502947+00:00'


b = {"date_end": "2017-01-29T15:59:59+00:00",
     "date_last_replied": null,
     "date_start": "2017-01-10T16:00:00+00:00",
     "description": "\u5927\u5bb6\u6765\u4fdd\u62a4\u773c\u775b\u505a\u773c\u4fdd\u5065\u64cd\u5427\uff5e\uff5e",
     "free_gift": 0,
     "id": "8034802801069747",
     "image": "http://easyread.ph.126.net/xHB3jbqjCtwgK8yMyVC0cw==/7917019182152835526.jpg",
     "is_participant": true,
     "is_respondent": false,
     "participants_count": 13,
     "price": 0,
     "replies_count": 0, "respondent": {
    "avatar": "https://medias.zaih.com/FpAMm0VzHUrK4oEoJx_n_MfwfaLM!avatar",
    "id": 589546902, "is_verified": true, "nickname": "\u59dc\u6653\u9e4f",
    "title": "\u5934\u8854\u7533\u8bf7\u4e2duuu\n"}, "respondent_id": 589546902,
     "share_title": null, "status": "public",
     "title": "\u6765\u505a\u773c\u4fdd\u5065\u64cd"}

c = {"date_end": "2017-01-06T10:21:08.948140+00:00",
     "date_last_replied": null,
     "date_start": "2017-01-06T10:21:08.948140+00:00",
     "description": "\u5c0f\u8bb2\u7b2c\u4e8c\u65e6\u5c0f\u8bb2\u7b2c\u4e8c\u65e6",
     "free_gift": 0,
     "id": "8034753806894251",
     "image": "https://medias.zaih.com/FoJApfJKG5gG9OgK7JuG34hbAnVr!preface",
     "is_participant": false,
     "is_respondent": false,
     "participants_count": 118,
     "price": 10,
     "replies_count": 0, "respondent": {
"avatar": "https://medias.zaih.com/909-917710246108-82-94-6-81526-7186-106!avatar",
"id": 589546892, "is_verified": true, "nickname": "jinying",
"title": "testtest"}, "respondent_id": 589546892,
     "share_title": null,
     "status": "public",
     "title": "\u5c0f\u8bb2\u7b2c\u4e8c\u65e6\u5c0f\u8bb2\u7b2c\u4e8c\u65e6"}