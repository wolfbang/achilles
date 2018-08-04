#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : redis-py.py
# @Author: lucas
# @Date  : 8/3/18
# @Desc  :

import redis
import logging

log_path = u'/Users/lucas/projects/achilles/logger.log'
logging.basicConfig(filename=log_path, level=logging.DEBUG)

client = redis.Redis(host=u'localhost', port=6379, db=0)


def query_info(section):
    infos = {}
    if section:
        infos = client.info(section)
    else:
        infos = client.info()
    print infos


def keys():
    keys = client.keys('*')
    print keys


def run():
    query_info('cpu')
    query_info('memory')
    query_info('connection')
    keys()


if __name__ == '__main__':
    run()
