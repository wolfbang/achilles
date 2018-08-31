#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gevent_power.py
# @Author: lucas
# @Date  : 8/31/18
# @Desc  :

import pprint
import gevent
import random


def task(pid):
    """non-deterministic task"""
    gevent.sleep(random.randint(0, 2) * 0.01)
    pprint.pprint('Task %s Done!' % pid)


def synchronous():
    pprint.pprint('Synchronous Worker:')
    for i in range(0, 10):
        task(i)


def asynchronous():
    pprint.pprint('Asynchronous Worker:')
    threads = [gevent.spawn(task, pid) for pid in range(0, 10)]
    gevent.joinall(threads)


def mock():
    synchronous()
    asynchronous()


def run():
    mock()


if __name__ == '__main__':
    run()
