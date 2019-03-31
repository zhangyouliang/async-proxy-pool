#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'youliangzhang'

from app.scheduler import run_schedule
from app.logger import setup_logging

setup_logging(default_path="util/logging.yaml")

run_schedule()