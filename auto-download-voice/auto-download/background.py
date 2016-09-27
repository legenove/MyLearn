# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os
import sys
import logging
import requests
import signal
from Queue import Queue
from multiprocessing import Process

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, "..", "site-packages"))

from redis_model.queue import Worker

from load_data import get_url, mp3_file


def do_download(data):
    file_name = data.get('file_name')
    vid = data.get('vid')
    key = data.get('key')
    source = data.get('source')
    store_type = data.get('store_type')
    status = data.get('status')
    mp3_path = mp3_file + file_name + '/'
    if not os.path.exists(mp3_path):
        os.mkdir(mp3_path)
    mp3_final_path = mp3_path + vid + ".mp3"
    if os.path.exists(mp3_final_path):
        logging.error(vid+":000::exist")
        return
    url = get_url(key, store_type=store_type, status=status, source=source)
    if url:
            r = requests.get(url, timeout=(30, 30))
            if r.status_code >= 400:
                logging.error(vid+":111::not found")
            else:
                try:
                    code = open(mp3_final_path, "wb")
                    code.write(r.content)
                    logging.error(data)
                except e:
                    logging.error(e)
                finally:
                    code.close()

    else:
        logging.error(vid+":33::not found")


if __name__ == "__main__":
    worker = Worker("background_download.mp3")
    try:
        worker.register(do_download)
        worker.start()
    except KeyboardInterrupt:
        worker.stop()
        print "exited cleanly"
        sys.exit(1)
    except Exception, e:
        print e
