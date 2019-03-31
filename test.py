#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'youliangzhang'

from sanic import Sanic, Blueprint
from sanic.response import text, json
from sanic.exceptions import NotFound

app = Sanic(__name__)


@app.route("/")
async def test(request):
    return text("hello world")


@app.route("/tag/<tag>")
async def test(request, tag):
    return text("Tag - {}".format(tag))


@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))


@app.route('/person/<name:[A-z]>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))


@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))


@app.route('/post', methods=['POST', 'GET'])
async def post_handler(request):
    return text("POST request - {}".format(request.json))


# 蓝图 blueprint
bp = Blueprint("my_blueprint")


@bp.route('/bp')
async def bp_root(request):
    return json({'my': 'blueprint'})


# 利用蓝图注册全局中间件
# @bp.middleware
# async def print_on_request(request):
#     print("I am a spy")

# @bp.middleware('request')
# async def halt_request(request):
#     return text('I halted the request')

# @bp.middleware('response')
# async def halt_response(request, response):
#     return text('I halted the response')


# 异常处理
@bp.exception(NotFound)
def ignore_404(request, exception):
    return text('404 Not Found')


app.blueprint(bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
