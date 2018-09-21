#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_threading_lock.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

import threading
import gevent
import random
from pprint import pprint

lock = threading._RLock()
total = 0


class SuperThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None, tid=1):
        super(SuperThread, self).__init__(group=group, target=target, name=name, args=args, kwargs=kwargs,
                                          verbose=verbose)
        self.tid = tid

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def calculate_with_lock():
    global total
    try:
        lock.acquire()
        total += 1
    finally:
        lock.release()


def calculate_without_lock():
    global total
    total += 1


def run_with_gevent():
    cal = calculate_with_lock
    cal_no_lock = calculate_without_lock

    task_list = [cal if random.randint(0, 10000) % 2 == 0 else cal_no_lock for x in range(0, 100)]
    spawns = [gevent.spawn(task) for task in task_list]
    gevent.joinall(spawns)


def run():
    for i in range(0, 1000):
        t = SuperThread(target=calculate_without_lock)
        t2 = SuperThread(target=calculate_without_lock)
        t3 = SuperThread(target=calculate_without_lock)
        t.start()
        t2.start()
        t3.start()

    pprint('[Total] %s' % total)
    run_with_gevent()
    pprint('[Total]run_with_gevent %s' % total)


if __name__ == '__main__':
    run()
