#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_performance_timer.py
# @Author: lucas
# @Date  : 9/29/18
# @Desc  :


from functools import wraps
from pprint import pprint
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pprint('[before] before execute')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        pprint('[after]executeTime: %s' % (end - start))
        return result

    return wrapper


def super_timer(permission):
    def _timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pprint('[before]func name: %s,%s' % (func.__name__, permission))
            result = func(*args, **kwargs)
            pprint('[after]decorated function finish executing!')
            return result

        return wrapper

    return _timer


@timer
@super_timer('permission')
def adder(x, y):
    return x + y


def run():
    pprint(adder(1, 3))


if __name__ == '__main__':
    run()
