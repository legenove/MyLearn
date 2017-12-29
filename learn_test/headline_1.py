# -*- coding:utf-8 -*-
import urllib2
import json
import codecs

# 访问头条接口，获取头条数据
response = urllib2.urlopen('http://fd.zaih.com/topline_api/v1/headlines')
# 受用json 读取返回信息，转化为json
res=json.loads(response.read())

for r in res:
    print r.get ('title')

# 把数据存入文件 a.csv
f=open('a.csv', "w")
f.write(codecs.BOM_UTF8)

tr="id,标题,简介,作者,作者id,地址\n"
f.write(tr)
# -*- coding:utf-8 -*-
base_url = 'http://fd.zaih.com/topline/'
for r in res:
    tr = ''
    tr=tr + r['id']+","
    tr = tr + r['title'] + ","
    if r['summary']:
        tr = tr + r['summary'] + ","
    else:
        tr += ","
    tr = tr+r['account']['nickname']+","
    tr = tr+str(r['account']['id'])+","
    tr = tr +base_url+r['id']+"\n"
    f.write(tr.encode('utf8'))



import time
from datetime import datetime

last = res[-1]
date_published = last['date_published']

# 把时间格式字符串，转化为时间戳
t = datetime.strptime(date_published, "%Y-%m-%dT%H:%M:%S.%f+00:00")
ts = time.mktime(t.timetuple())

# 进行拼接
start_key = 'create_time=' + str(ts) + \
            "&date_published=" + date_published + \
            "&hash_name=headline"

print start_key

import base64

start_key = base64.urlsafe_b64encode(start_key)

print start_key
# 拼接 url
params = 'start_key=' + start_key + '&limit=20'

url = 'http://fd.zaih.com/topline_api/v1/headlines?' + params

# 访问头条接口，获取头条数据
response = urllib2.urlopen(url)
# 受用json 读取返回信息，转化为json
res=json.loads(response.read())

print res
for r in res:
    print r.get('title')
