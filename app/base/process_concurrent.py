#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : process_concurrent.py
# @Author: lucas
# @Date  : 9/20/18
# @Desc  :

from pprint import pprint
import threading

rock = threading.RLock()

balance = 100


def mock_withdraw(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(0, 10000):
        rock.acquire()
        try:
            mock_withdraw(n)
        finally:
            rock.release()
        pprint('%s,%s' % (balance, threading.currentThread().getName()))


def run():
    t1 = threading.Thread(target=run_thread, args=(5,), name='Th-Mock-1')
    t2 = threading.Thread(target=run_thread, args=(8,), name='Th-Mock-2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pprint('[Result] %s' % balance)


if __name__ == '__main__':
    run()
