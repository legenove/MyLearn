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

from load_data import voice_path, bad_path, split_str, mp3_file,get_url

queue_client = Client()

def download_mp3(begin=None, end=None):
    voice_files = os.listdir(voice_path)
    count = 0
    if begin is not None and end is not None:
        voice_files = voice_files[begin:end]
    print len(voice_files)
    for voice_file in voice_files:
        with open(voice_path + voice_file, 'r') as voice_infos:
            for info in voice_infos.readlines():
                info_list = info.strip('\n').split(split_str)
                data = {
                    'vid': info_list[0],
                    'key': info_list[1],
                    'source': info_list[2],
                    'store_type': info_list[3],
                    'status': info_list[4],
                }

                queue_client.dispatch("background_download.mp3", data)
                count += 1
    print count

if __name__ == '__main__':
    try:
        begin = int(sys.argv[1])
    except:
        begin = None
    try:
        end = int(sys.argv[2])
    except:
        end = None

    download_mp3(begin,end)


