#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_for_fun.py
# @Author: lucas
# @Date  : 9/28/18
# @Desc  :


from functools import wraps
from pprint import pprint


def decorator(uid=None, time=None):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pprint('DECORATOR args:%s,%s' % (uid, time))
            if not (time is not None and isinstance(time, int) and time <= 5):
                return

            result = func(*args, **kwargs)
            return result

        return wrapper

    return real_decorator


@decorator(uid=897654, time=5)
def do_cache():
    pprint('do cache now')


def run():
    do_cache()


if __name__ == '__main__':
    run()
