#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_manage_queue.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

import random, time, Queue
from multiprocessing.managers import BaseManager
from pprint import pprint


class QueueManger(BaseManager):
    pass


task_queue = Queue.Queue()
result_queue = Queue.Queue()

QueueManger.register('get_task_queue', callable=lambda: task_queue)
QueueManger.register('get_result_queue', callable=lambda: result_queue)

manager = QueueManger(address=('', 5000), authkey='abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()


for i in range(0, 100):
    pprint('put task %s' % i)
    task.put(i)

pprint('try get task')
for i in range(0, 100):
    r = task.get(timeout=1)
    result.put(r)
    pprint('Get task %s' % r)


def run():
    pprint(result.qsize())


if __name__ == '__main__':
    run()
