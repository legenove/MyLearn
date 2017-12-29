# -*-coding:utf-8-*-

import urllib2
import json
import base64
import time
from datetime import datetime

base_url = 'http://fd.zaih.com/topline/'

response = urllib2.urlopen("http://fd.zaih.com/topline_api/v1/headlines")
res = json.loads(response.read())
#
#
# for r in res:
#     tr = ""
#     tr = tr + r['id'] + ","
#     tr = tr + r['title'] + ","
#     tr = tr + r['summary'] + ","
#     tr = tr + r['account']['nickname'] + ","
#     tr = tr + str(r['account']['id']) + ","
#     tr = tr + base_url+r['id'] + "\n"
#     f.write(tr.encode('utf8'))
#
# f.close()


f = open('a.csv', "w")
tr = "id,标题,简介,声音,作者,作者id,地址\n"
f.write(tr)

def get_headline(url, params):
    response = urllib2.urlopen(url + '?'+ params)
    return json.loads(response.read())

def save_to_csv(f,res):
    print res
    for r in res:
        tr = ""
        tr = tr + r['id'] + ","
        tr = tr + r['title'] + ","
        if r['summary']:
            tr = tr + r['summary'] + ","
        else:
            tr += ","
        if r['voice']:
            tr += u'是,'
        else:
            tr += u"否,"
        tr = tr + r['account']['nickname'] + ","
        tr = tr + str(r['account']['id']) + ","
        tr = tr + base_url+r['id'] + "\n"
        f.write(tr.encode('utf8'))

def get_params(res):
    last = res[-1]
    date_published = last['date_published']
    t = datetime.strptime(date_published, "%Y-%m-%dT%H:%M:%S.%f+00:00")
    ts = time.mktime(t.timetuple())
    start_key = "create_time=%s&date_published=%s&hash_name=headline" % (ts ,date_published)
    start_key = base64.urlsafe_b64encode(start_key)
    params = "start_key=%s&limit=20" % start_key
    return params

url = "http://fd.zaih.com/topline_api/v1/headlines"
params = ""
while True:
    res = get_headline(url, params)
    if not res:
        break
    save_to_csv(f, res)
    params = get_params(res)

