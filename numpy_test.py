# -*- coding: utf-8 -*-

import numpy

A = [
    [1, 3, 4],
    [3, 2, 5]
]
B = [
    [1, 3],
    [3, 2],
    [3, 1]
]

print numpy.dot(A, B)

import zipfile

_file = zipfile.ZipFile('123.zip', 'w', zipfile.ZIP_STORED)
_file.write('./fenda.all.com')
_file.setpassword('12345678')
_file.close()

import pyminizip

import os

kw = {
    'password': '12345678',
    'zip_filename': 'dst.zip',
    'filename': './fenda.all.com'
}

s = 'zip -P {password} {zip_filename} {filename}'.format(**kw)

os.system(s)

kw.update(filename='./fenda.all.com-2')

s = 'zip -P {password} {zip_filename} {filename}'.format(**kw)

os.system(s)
# compression_level = 5 # 1-9
#
# pyminizip.compress("./fenda.all.com", "dst.zip", "password", compression_level)
# _file = zipfile.ZipFile('123.zip', 'r')
# _file.setpassword('123')
# _file.close()
# import codecs
# codecs.open()

a = [{u'main_card_question_id': u'90000034251589279208',
      u'main_card_answer_nickname': u'tester',
      u'main_card_albums_id': u'1034078378390498',
      u'main_card_short_title': u'\u5934\u6761test\uff0d\uff0d\u95ee\u9898\u77ed\u6807\u9898'},
     {u'main_card_question_id': u'90000034252949823136',
      u'main_card_answer_nickname': u'\u90ed\u51ac\u6885',
      u'main_card_albums_id': u'1034078378390498',
      u'main_card_short_title': u'\u6768\u5e42\u5218\u607a\u5a01\u7684\u771f\u662f\u7231\u60c5\u6545\u4e8b'}]