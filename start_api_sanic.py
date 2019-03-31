#!/usr/bin/env python
# coding=utf-8

from api.webapi_sanic import app
from app.config import SERVER_HOST, SERVER_PORT, SERVER_ACCESS_LOG

from app.logger import setup_logging

setup_logging(default_path="util/logging.yaml")
# 启动服务端 Sanic app
app.run(host=SERVER_HOST, port=SERVER_PORT, access_log=SERVER_ACCESS_LOG)
