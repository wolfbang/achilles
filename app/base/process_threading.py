#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_threading.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

import threading
from pprint import pprint


def loop():
    pprint('Thread %s is running' % threading.current_thread().getName())
    n = 0
    while n < 5:
        n = n + 1
        pprint('Thread %s >>>> %s' % (threading.currentThread().getName(), n))

    pprint('Thread %s end' % (threading.currentThread().getName()))


def execute():
    pprint('Thread %s is running' % (threading.current_thread().getName()))
    t = threading.Thread(target=loop, name='ConcurrentLoop')
    t.start()
    t.join()
    pprint('Thread %s end' % threading.current_thread().getName())


def run():
    loop()


if __name__ == '__main__':
    run()
