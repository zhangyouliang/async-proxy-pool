#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "youliangzhang"
'''
定义几个关键字，count type,protocol,country,area,
'''
import json
import sys
import config
from db.DataStore import sqlhelper
from db.SqlHelper import Proxy
from flask import Flask
from flask import request
from flask_script import Manager
from flask import Blueprint
router = Blueprint('router', __name__)


@router.route("/getProxy", methods=['GET'])
def getProxy():
    count = request.args.get('count', 1)
    datax = request.args.to_dict()
    data = []
    for item in sqlhelper.select(count, datax):
        data.append({
            "ip": item[0],
            "port": item[1],
            "protocol": 'http' if item[2] == 0 else 'https',
            "country": item[4],
            "area": item[5],
            "updatetime": item[6].strftime("%Y-%m-%d %H:%M:%S"),
            "speed": item[7].__str__(),
            "score": item[3],
        })
    json_result = json.dumps(data)
    return json_result


# 获取真实 ip
def getRealIp():
    if request.headers.get('X-Forwarded-For') is not None:
        ip = request.headers.get('X-Forwarded-For')
    elif request.headers.get('X-Real-IP') is not None:
        ip = request.headers.get('X-Real-IP')
    else:
        ip = request.remote_addr
    return ip


@router.route("/", methods=["GET", "POST"])
def getIp():
    return getRealIp()


# 获取用户IP等信息
@router.route("/get", methods=["GET", "POST"])
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


# @router.route("/delete", methods=['GET'])
# def delete():
#     inputs = request.args.to_dict()
#     json_result = json.dumps(sqlhelper.delete(inputs))
#     return json_result
