#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_performance.py
# @Author: lucas
# @Date  : 9/24/18
# @Desc  :

from pprint import pprint
import functools
import time


def performance(func):
    @functools.wraps(func)
    def fn(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        pprint('call %s in %fs' % (func.__name__, end - start))
        return r

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def run():
    result = factorial(3)
    pprint(result)


if __name__ == '__main__':
    run()
