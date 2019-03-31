#!/usr/bin/env python
# coding=utf-8

from sanic import Sanic
from sanic.response import json, text

from app.database import RedisClient

app = Sanic()
redis_conn = RedisClient()


# 获取真实 ip
def getRealIp(request):
    if request.headers.get('X-Forwarded-For') is not None:
        ip = request.headers.get('X-Forwarded-For')
    elif request.headers.get('X-Real-IP') is not None:
        ip = request.headers.get('X-Real-IP')
    else:
        ip = '127.0.0.1' if request.remote_addr == '' else request.remote_addr
    return ip


# 获取用户IP等信息
@app.route("/origin", methods=["GET", "POST"])
def getOrigin(request):
    headers = dict(request.headers)
    if headers.get('cookie'):
        del (headers['cookie'])

    data = {
        "args": request.args,
        "headers": headers,
        "origin": getRealIp(request),
        "url": request.url
    }
    return json(data)


@app.route("/")
async def index(request):
    # print(dir(request))
    print(request.__dir__)
    return text(getRealIp(request))


@app.route("/pop")
async def pop_proxy(request):
    proxy = redis_conn.pop_proxy().decode("utf8")
    if proxy[:5] == "https":
        return json({"https": proxy})
    else:
        return json({"http": proxy})


@app.route("/get/<count:int>")
async def get_proxy(request, count):
    res = []
    for proxy in redis_conn.get_proxies(count):
        if proxy[:5] == "https":
            res.append({"https": proxy})
        else:
            res.append({"http": proxy})
    return json(res)


@app.route("/count")
async def count_all_proxies(request):
    count = redis_conn.count_all_proxies()
    return json({"count": str(count)})


@app.route("/count/<score:int>")
async def count_score_proxies(request, score):
    count = redis_conn.count_score_proxies(score)
    return json({"count": str(count)})


@app.route("/clear/<score:int>")
async def clear_proxies(request, score):
    if redis_conn.clear_proxies(score):
        return json({"Clear": "Successful"})
    return json({"Clear": "Score should >= 0 and <= 10"})
