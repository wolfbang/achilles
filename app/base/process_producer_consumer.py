#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_producer_consumer.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

import os
import time
import random

from multiprocessing import Process, Queue
from pprint import pprint


def write(queue):
    for value in ['A', 'B', 'C']:
        pprint('Put %s to Queue' % value)
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    while True:
        item = queue.get(True)
        pprint('Get %s from Queue' % item)


def run():
    queue = Queue()
    qw = Process(target=write, args=(queue,))
    qr = Process(target=read, args=(queue,))

    qw.start()
    qr.start()
    qw.join()

    qr.terminate()


if __name__ == '__main__':
    run()
