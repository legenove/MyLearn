# -*- coding: utf-8 -*-

import sys, os
from werkzeug.serving import BaseRequestHandler
from flask.ext.script import Manager, Server

from base.settings import settings, create_app


app = create_app(True, False, 'base', 'weixinapp')
manager = Manager(app)

manager.add_command('server', Server(host='0.0.0.0', port=settings['PORT'],
                                     use_reloader=True, threaded=True,
                                     request_handler=BaseRequestHandler))

if __name__ == '__main__':
    manager.run()