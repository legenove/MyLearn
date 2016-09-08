
import os
import signal
from tornado import web, ioloop
import datetime
import time
import threading
from multiprocessing import Process
from Queue import Queue
period = 5 * 1000   # every 5 s
class MainHandler(web.RequestHandler):
    def get(self):
        self.write('Hello Tornado')
def like_cron():
    print datetime.datetime.now()
def xiaorui():
    time.sleep(10)
    print 'xiaorui 10s'






def lee():
    print 'lee 100s start'
    time.sleep(100)
    print 'lee 100s stop'

def thread_task():
    t = threading.Thread(target=lee)
    t.setDaemon(True)
    t.start()

q = Queue(4)
a = ioloop.PeriodicCallback(like_cron, period)
def process_task():
    while not q.empty():
        p = q.get_nowait()
        if p.is_alive():
            print "kill pid:" + str(p.pid)
            os.kill(p.pid, signal.SIGKILL)
    p = Process(target=lee)
    p.start()
    q.put(p)
    a.stop()


if __name__ == '__main__':
    application = web.Application([
        (r'/', MainHandler),
        ])
    application.listen(8081)
    a.start()  # start scheduler
    ioloop.PeriodicCallback(process_task, 10000).start()  # start scheduler
    ioloop.IOLoop.instance().start()