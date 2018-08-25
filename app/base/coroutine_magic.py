#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : coroutine_magic.py
# @Author: lucas
# @Date  : 8/24/18
# @Desc  :


import pprint


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 100:
            break


def grep(pattern):
    pprint.pprint('search for {pattern}'.format(pattern=pattern))
    while True:
        line = yield
        if pattern in line:
            pprint.pprint(pattern)


def __mock():
    for i in fib():
        pprint.pprint(i)


def run():
    __mock()

    search = grep('coroutine')
    next(search)
    search.send('hello')
    search.send('rou')
    search.send('i love coroutine very much!')
    search.close()


if __name__ == '__main__':
    run()
