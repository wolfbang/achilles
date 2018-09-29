#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_multiply_with_args.py
# @Author: lucas
# @Date  : 9/29/18
# @Desc  :

from functools import wraps
from pprint import pprint


def multiply(by=None):
    def _multiply(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pprint('[Wrapper] invoked,by=%s' % by)
            result = by * func(*args, **kwargs)
            return result

        return wrapper

    return _multiply


@multiply(by=3)
def adder(x, y):
    return x + y


def duplicate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = 2 * func(*args, **kwargs)
        return result

    return wrapper


def formatting(lowercase=False):
    def _formatting(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if lowercase:
                return str(result).lower()
            return result

        return wrapper

    return _formatting


@duplicate
@formatting(lowercase=True)
def get_message(message):
    return message


def run():
    pprint(adder(1, 3))
    pprint(get_message('GOOD JOB!'))


if __name__ == '__main__':
    run()
