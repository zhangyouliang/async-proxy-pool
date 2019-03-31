#!/usr/bin/env python
# coding=utf-8

from flask import Flask, jsonify, request
from app.database import RedisClient
import json

app = Flask(__name__)
redis_conn = RedisClient()


# 获取真实 ip
def getRealIp():
    if request.headers.get('X-Forwarded-For') is not None:
        ip = request.headers.get('X-Forwarded-For')
    elif request.headers.get('X-Real-IP') is not None:
        ip = request.headers.get('X-Real-IP')
    else:
        ip = request.remote_addr
    return ip


@app.route("/")
def index():
    return getRealIp()


# 获取用户IP等信息
@app.route("/origin", methods=["GET", "POST"])
def getOrigin():
    headers = dict(request.headers)
    if headers.get('Cookie'):
        del (headers['Cookie'])

    data = {
        "args": request.values.to_dict(),
        "headers": headers,
        "origin": getRealIp(),
        "url": request.url
    }
    return json.dumps(data)


@app.route("/pop")
def pop_proxy():
    proxy = redis_conn.pop_proxy().decode("utf8")
    if proxy[:5] == "https":
        return jsonify({"https": proxy})
    else:
        return jsonify({"http": proxy})


@app.route("/get/<int:count>")
def get_proxy(count):
    res = []
    for proxy in redis_conn.get_proxies(count):
        if proxy[:5] == "https":
            res.append({"https": proxy})
        else:
            res.append({"http": proxy})
    return jsonify(res)


@app.route("/count")
def count_all_proxies():
    count = redis_conn.count_all_proxies()
    return jsonify({"count": str(count)})


@app.route("/count/<int:score>")
def count_score_proxies(score):
    count = redis_conn.count_score_proxies(score)
    return jsonify({"count": str(count)})


@app.route("/clear/<int:score>")
def clear_proxies(score):
    if redis_conn.clear_proxies(score):
        return jsonify({"Clear": "Successful"})
    return jsonify({"Clear": "Score should >= 0 and <= 10"})
