#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_elegant_args.py
# @Author: lucas
# @Date  : 10/1/18
# @Desc  :

from functools import wraps
from pprint import pprint


def elegant_args(*args_func, **kwargs_func):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pprint('decorator args:%s,kwargs:%s' % (args_func, kwargs_func))
            pprint('func args:%s,kwargs:%s' % (args, kwargs))
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@elegant_args('chaos', name='simpson', address='California,USA')
def adder(x, y):
    return x + y


def run():
    pprint(adder(1, 6))


if __name__ == '__main__':
    run()
