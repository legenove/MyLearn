# -*- coding: utf-8 -*-

import os
import sys
import signal
import requests
from Queue import Queue
from multiprocessing import Process

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, "..", "site-packages"))

from redis_model.queue import Client

from load_data import voice_path, bad_path, split_str, mp3_file, get_url

queue_client = Client()


def download_mp3(begin=None, end=None):
    voice_files = os.listdir(voice_path)
    if begin is not None and end is not None:
        voice_files = voice_files[begin:end]
    for voice_file in voice_files:
        file_name = voice_file.split('.')[0]
        mp3_path = mp3_file + file_name + '/'
        exist_path = False
        if os.path.exists(mp3_path):
            exist_path = True
        with open(voice_path + voice_file, 'r') as voice_infos:
            for info in voice_infos.readlines():
                info_list = info.strip('\n').split(split_str)
                data = {
                    'file_name': file_name,
                    'vid': info_list[0],
                    'key': info_list[1],
                    'source': info_list[2],
                    'store_type': info_list[3],
                    'status': info_list[4],
                }
                if exist_path:
                    mp3_final_path = mp3_path + info_list[0] + ".mp3"
                    if os.path.exists(mp3_final_path):
                        continue
                queue_client.dispatch("background_download.mp3", data)


if __name__ == '__main__':
    try:
        begin = int(sys.argv[1])
    except:
        begin = None
    try:
        end = int(sys.argv[2])
    except:
        end = None

    download_mp3(begin, end)


