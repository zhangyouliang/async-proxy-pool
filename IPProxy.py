#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "youliangzhang"

import warnings
warnings.filterwarnings("ignore")
from multiprocessing import Value, Queue, Process
from api.apiServer import start_api_server
from db.DataStore import store_data

from validator.Validator import validator, getMyIP
from spider.ProxyCrawl import startProxyCrawl

from config import TASK_QUEUE_SIZE
from util.logger import setup_logging
import logging
if __name__ == "__main__":
    setup_logging(default_path="util/logging.yaml")
    myip = getMyIP()
    logging.info(myip)
    DB_PROXY_NUM = Value('i', 0)
    # 爬取队列
    q1 = Queue(maxsize=TASK_QUEUE_SIZE)
    # 验证队列
    q2 = Queue()
    p0 = Process(target=start_api_server)
    p1 = Process(target=startProxyCrawl, args=(q1, DB_PROXY_NUM, myip))
    p2 = Process(target=validator, args=(q1, q2, myip))
    p3 = Process(target=store_data, args=(q2, DB_PROXY_NUM))
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p0.join()
    p1.join()
    p2.join()
    p3.join()