#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_log_aop.py
# @Author: lucas
# @Date  : 8/17/18
# @Desc  :



from functools import wraps
import pprint


def logit(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        pprint.pprint('{func_name} is called'.format(func_name=func.__name__))
        return func(*args, **kwargs)

    return wrap_func


@logit
def add(x, y):
    if not (x and y):
        return
    return x + y


def run():
    """do some math"""
    result = add(3, 5)
    pprint.pprint(add.__name__)
    pprint.pprint(result)


if __name__ == '__main__':
    run()
