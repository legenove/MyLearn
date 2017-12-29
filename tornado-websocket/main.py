# -*- coding: utf-8 -*-

import time
import logging
import signal
import tornado.options
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket



def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)

def shutdown():
    logging.info('Stopping http server')

    logging.info('Will Shutdown in %s seconds ...', 60)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + 60

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            logging.info('Shutdown')
    stop_loop()

def init_options(port=8080, worker=1, debug=False, doc=False, timeout=2):
    tornado.options.define('port', default=port, type=int)
    tornado.options.define('worker', default=worker, type=int)
    tornado.options.define('debug', default=debug, type=bool)
    tornado.options.define('doc', default=doc, type=bool)
    tornado.options.define('timeout', default=timeout, type=int)
    tornado.options.parse_command_line()

    return tornado.options.options

def main(**kwargs):

    _options = init_options(**kwargs)
    print _options

    http_server = tornado.httpserver.HTTPServer(tornado.web.Application())
    http_server.listen(8000)
    logging.info('start listen on port: %s', 8000)
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()