#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "youliangzhang"
import yaml
import logging, logging.config, coloredlogs
import os


def setup_logging(default_path='logging.yaml',
                  default_level=logging.INFO,
                  env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'r') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
            fmt = config.get('formatters').get('simple').get('format')
            coloredlogs.install(milliseconds=True, fmt=fmt)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(
            milliseconds=True,
            fmt=
            '%(asctime)s - [%(module)s:%(funcName)s():%(lineno)d] - %(levelname)s - %(message)s'
        )
