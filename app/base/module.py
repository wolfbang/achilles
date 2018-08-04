#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : module.py
# @Author: lucas
# @Date  : 8/4/18
# @Desc  :


import pprint
import sys

from app.base import redis_client

sys.path.append('')


def get_power():
    return 'power'


def get_path():
    path = sys.path
    pprint.pprint(path)


def get_redis():
    redis_info = redis_client
    print redis_info


def run():
    get_path()
    get_redis()


if __name__ == '__main__':
    run()
