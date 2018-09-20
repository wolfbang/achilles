#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_func.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

import os
from multiprocessing import Process
from pprint import pprint


def sys_process():
    pid = os.getpid()
    pprint('Process %s start' % pid)

    new_pid = os.fork()
    pprint(new_pid)
    if new_pid == 0:
        pprint('[Sub process]I\'m sub process:%s,and my parent pid:%s' % (os.getpid(), os.getppid()))
    else:
        pprint('I am %s, and I just create a pid:%s' % (os.getpid(), pid))


def run_proc(name):
    return 'run child process %s,%s' % (name, os.getpid())


def multi_processing():
    p = Process(target=run_proc, args=('test',))
    pprint('[Process] start')
    p.start()
    p.join()
    pprint('[Process] end')


def run():
    sys_process()
    multi_processing()


if __name__ == '__main__':
    run()
