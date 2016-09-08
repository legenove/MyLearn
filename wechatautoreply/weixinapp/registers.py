# -*- coding: utf-8 -*-

from flask import Flask
from base.settings import Config


def create_app(register_bp=True, test=False):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    if test:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True

    # TODO: 接入数据库后需要配置
    # register_extensions(app)
    # TODO: if need
    # register_after_request(app)

    if register_bp:
        register_blueprints(app)
    if test:
        @app.route('/')
        def index():
            return 'Index Page'
    return app


def register_blueprints(app):
    from view import wechat

    app.register_blueprint(wechat.instance_wechat, url_prefix='/wechat')


def register_extensions(app):
    # TODO: 接入数据库后需要配置
    pass


def register_after_request(app):
    # TODO: if need
    pass


if __name__ == "__main__":
    app = create_app(test=True)
    app.run()