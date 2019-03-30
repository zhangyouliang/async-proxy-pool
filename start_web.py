#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'youliangzhang'

from flask import Flask
from flask import request
from flask_script import Manager

########  router
from api.router import router

app = Flask(__name__)
app.config.update(DEBUG=False)
manager = Manager(app)
app.register_blueprint(router, url_prefix='')


# 正式部署
def start_api_server():
    app.run()


# python start_web.py dev
# 实现自动刷新调试功能
@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False, host='0.0.0.0')


if __name__ == '__main__':
    start_api_server()