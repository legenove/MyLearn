# -*- coding: utf-8 -*-

import os
import sys
import signal
from Queue import Queue
from multiprocessing import Process

from db import zhifubao_db,censor_db

STATUS_DRAFT = 'draft'
STATUS_SUCCEED = 'succeed'

SOURCE_WEIXIN = 'weixin'

voice_path = "../voice/"
bad_path = "../bad/"
voice_file_name = "voice_url_%d.txt"
split_str = ":$??:"
mp3_file = "/Users/legenove/GuokrWorkSpace/Other/mp3_files/"
# mp3_file = "/Volumes/Samsung_T3/mp3_files/"


class QusetionData(object):
    question_sql = "SELECT question.id AS question.id, account_1.id AS respondent_id, account_1.nickname AS respondent_nickname, account_2.id AS asker_id,account_2.nickname AS asker_nickname,question.content,question._visitor_count AS visitor_count, answer.id AS answer_id,voice.id AS voice_id FROM question " \
                   "INNER JOIN account AS account_1 ON account_1.id = question.respondent_id " \
                   "INNER JOIN account AS account_2 ON account_2.id = question.account_id " \
                   "INNER JOIN answer ON answer.question_id = question.id  " \
                   "FULL JOIN voice ON voice.target_id= answer.id  " \
                   "WHERE respondent_id in (588999836,594103712,594084309,588137519,594004726,588157702,588767184,592901052) AND " \
                   "question.review_status='passed' " \
                   "AND question._visitor_count>50 " \
                   "ORDER BY question._visitor_count DESC LIMIT 100;"

    def __init__(self, limit=10000, start_page=0):
        self.limit = limit
        self.offset = start_page * limit

    def _get_sql(self, offset=None):
        if offset is None:
            sql = self.question_sql
        else:
            sql = self.question_sql
        return sql

    def get_data(self, offset=None):
        sql = self._get_sql(offset=offset)
        ret, questions = zhifubao_db.query(sql)
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

class VoiceData(object):
    question_sql = "select voice_id,content from voice_content where voice_id in %s;"

    def __init__(self, limit=10000, start_page=0):
        self.limit = limit
        self.offset = start_page * limit

    def _get_sql(self, offset=None):
        if offset is None:
            sql = self.question_sql
        else:
            sql = self.question_sql
        return sql

    def get_data(self, offset=None):
        sql = self._get_sql(offset=offset)
        ret, questions = censor_db.query(sql)
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
    for index, question in enumerate(qusetion_datas):
        my_question = question
        break

    # count, files = save_voice_url(qusetion_datas)
    # print "-----", count, files