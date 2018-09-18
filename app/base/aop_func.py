#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aop_func.py
# @Author: lucas
# @Date  : 9/18/18
# @Desc  :

import inspect
import functools
from pprint import pprint


def aspectize(arg):
    def decorate_method(func):
        func.__before = []
        func.__after = []

        def decorated(*args, **kwargs):
            for f in func.__before:
                res = f(*args, **kwargs)
                if res is not None:
                    return res

            main_res = func(*args, **kwargs)

            for f in func.__after:
                res = f(*args, **kwargs)
                if res is not None:
                    return res

            return main_res

        decorated.__before = func.__before
        decorated.__after = func.__after

        return decorated

    if inspect.isclass(arg):
        for attr in arg.__dict__:
            if callable(arg.__dict__[attr]):
                setattr(arg, attr, decorate_method(arg.__dict__[attr]))

    elif callable(arg):
        return decorate_method(arg)

    else:
        raise Exception("[Error]don't know what to do with this argument! ")


def before(method):
    def decorator(advice):
        method.__before.append(advice)

    return decorator


def after(method):
    def decorator(advice):
        method.__after.append(advice)

    return decorator
