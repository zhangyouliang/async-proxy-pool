#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'youliangzhang'
from config import QQWRY_PATH, CHINA_AREA
from util.IPAddress import IPAddresss
from util.compatibility import text_


def main():
    ips = IPAddresss(QQWRY_PATH)
    ip = '116.230.127.28'

    addr = ips.getIpAddr(ips.str2ip(ip))
    print(addr)


if __name__ == '__main__':
    main()
