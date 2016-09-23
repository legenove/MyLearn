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
    vid = data.get('vid')
    key = data.get('key')
    source = data.get('source')
    store_type = data.get('store_type')
    status = data.get('status')
    url = get_url(key, store_type=store_type, status=status, source=source)
    if url:
        try:
            r = requests.get(url)
            if r.status_code >= 400:
                logging.error(vid+":not found")
            else:
                logging.error(data)
                with open(mp3_file + vid + ".mp3", "wb") as code:
                    code.write(r.content)
        except:
            logging.error(vid+"not found")


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
