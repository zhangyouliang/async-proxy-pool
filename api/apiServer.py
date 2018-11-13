# coding:utf-8
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

app = Flask(__name__)
app.config.update(DEBUG=False)

@app.route("/",methods=['GET'])
def home():
    count = request.args.get('count',None)
    datax = request.args.to_dict()
    json_result = json.dumps(sqlhelper.select(count, datax))
    return json_result

@app.route("/delete",methods=['GET'])
def delete():
    inputs = web.input()
    json_result = json.dumps(sqlhelper.delete(inputs))
    return json_result


def start_api_server():
    app.run()

if __name__ == '__main__':
    start_api_server()
