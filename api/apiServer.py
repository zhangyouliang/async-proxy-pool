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


@app.route("/", methods=['GET'])
def home():
    count = request.args.get('count', 1)
    datax = request.args.to_dict()
    print(sqlhelper.select(count, datax))
    data = []
    for item in sqlhelper.select(count, datax):
        print(dir())
        print(dir(item[7]))
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


# @app.route("/delete", methods=['GET'])
# def delete():
#     inputs = request.args.to_dict()
#     json_result = json.dumps(sqlhelper.delete(inputs))
#     return json_result


def start_api_server():
    app.run(port=8000)


if __name__ == '__main__':
    start_api_server()
