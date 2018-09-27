#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_with_arguments.py
# @Author: lucas
# @Date  : 9/27/18
# @Desc  :


from functools import wraps
from pprint import pprint


def handle_decorator_args(*args):
    pprint('handle and print args:%s' % args)
    pass


def decorator(argument):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pprint('before')
            pprint('decorated method_name:%s' % func.func_name)
            handle_decorator_args(argument)
            result = func(*args, **kwargs)
            pprint('after')
            return result

        return wrapper

    return real_decorator


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pprint('do a second decoration1')
        return func(*args, **kwargs)

    return wrapper


@decorator2
@decorator('session_commit')
def commit():
    pprint('do commit...')
    return "[return statement]"


def run():
    pprint(commit())


if __name__ == '__main__':
    run()
