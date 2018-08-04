#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : module-py.py
# @Author: lucas
# @Date  : 8/4/18
# @Desc  :


import sys
import base
import pprint

sys.path.append('')


def get_power():
    return 'power'


def get_path():
    path = sys.path
    pprint.pprint(path)


def get_redis():
    redis_info = base
    print redis_info


def run():
    get_path()
    get_redis()


if __name__ == '__main__':
    run()
