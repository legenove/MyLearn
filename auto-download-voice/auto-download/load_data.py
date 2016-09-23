# -*- coding: utf-8 -*-

import os
import sys
import signal
from Queue import Queue
from multiprocessing import Process

from db import PostgreSQL

STATUS_DRAFT = 'draft'
STATUS_SUCCEED = 'succeed'

SOURCE_WEIXIN = 'weixin'

_db = PostgreSQL()
voice_path = "../voice/"
bad_path = "../bad/"
voice_file_name = "voice_url_%d.txt"
split_str = ":$??:"
mp3_file = "/Users/legenove/GuokrWorkSpace/Other/mp3_files/"


class QusetionData(object):
    question_sql = "SELECT id FROM question WHERE " \
                   "is_hidden=FALSE AND " \
                   "status IN ('succeed','answered') AND" \
                   " review_status IN ('passed','auto_passed') OFFSET %s LIMIT %s;"

    def __init__(self, limit=10000, start_page=0):
        self.limit = limit
        self.offset = start_page * limit

    def _get_sql(self, offset=None):
        if offset is None:
            sql = self.question_sql % (0, self.limit)
        else:
            sql = self.question_sql % (offset, self.limit)
        return sql

    def get_data(self, offset=None):
        sql = self._get_sql(offset=offset)
        ret, questions = _db.query(sql)
        return questions

    def __iter__(self):
        return self

    def next(self):

        self.questions = self.get_data(self.offset)
        if self.questions:
            if self.limit < 20:
                self.offset += 100000
            else:
                self.offset += self.limit
            return self.questions
        raise StopIteration()


def get_url(voice_key, store_type, status, source, expires=1800):
    from media import media_for, qiniu_private_url_gen

    if store_type == 'private':
        if status == STATUS_DRAFT and source == SOURCE_WEIXIN:
            return ''
        else:
            return qiniu_private_url_gen(voice_key, expires=expires)
    else:
        if source == SOURCE_WEIXIN:
            if voice_key and status == STATUS_SUCCEED:
                return media_for(voice_key)
            elif voice_key and status == STATUS_DRAFT:
                return media_for(voice_key, format_type='amr')
            else:
                return ''
        else:
            # 不是微信来源都认为是七牛
            return media_for(voice_key)


def save_voice_url(qusetion_datas):
    count = 0
    files = 0
    for index, question in enumerate(qusetion_datas):
        with open(voice_path + voice_file_name % index, 'w') as voice_file:
            voice_urls = []
            question_ids = [q[0] for q in question]
            sql = "SELECT id FROM answer WHERE" \
                  " question_id IN %s AND" \
                  " type = 'answer' AND" \
                  " status IN ('succeed');" % str(tuple(question_ids))

            # print sql

            ret, answers = _db.query(sql)
            if ret:
                answer_ids = [a[0] for a in answers if a[0] is not None]
                while answer_ids:

                    sql = "SELECT id,voice_key,source,store_type,status FROM voice WHERE" \
                          " target_id IN %s;" % str(tuple(answer_ids[:6000]))
                    answer_ids = answer_ids[6000:]

                    ret, voices = _db.query(sql)
                    if ret:
                        for voice in voices:
                            try:
                                voice_urls.append(split_str.join(voice) + '\n')
                                count += 1
                            except TypeError:
                                pass
                            # url = get_url(voice[1], store_type=voice[3], status=voice[4], source=voice[2])
                            # if url:
                            # voice_urls.append(voice[0] + split_str + url + '\n')
                            #     count += 1
            voice_file.writelines(voice_urls)
            files += 1
        print files, count
    return count, files


if __name__ == "__main__":
    try:
        limit = sys.argv[1]
    except:
        limit = 10000
    try:
        start_page = sys.argv[2]
    except:
        start_page = 0
    qusetion_datas = QusetionData(int(limit), start_page=0)
    count, files = save_voice_url(qusetion_datas)
    print "-----", count, files