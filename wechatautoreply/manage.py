# -*- coding: utf-8 -*-

from werkzeug.serving import BaseRequestHandler
from flask.ext.script import Manager, Server

from weixinapp.app import create_app
from base.settings import settings

app = create_app(test=True)
manager = Manager(app)



manager.add_command('server', Server(host='0.0.0.0', port=settings['PORT'],
                                     use_reloader=True, threaded=True,
                                     request_handler=BaseRequestHandler))

if __name__ == '__main__':
    manager.run()