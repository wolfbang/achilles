#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : function_tool_magic.py
# @Author: lucas
# @Date  : 9/18/18
# @Desc  :


import functools
from pprint import pprint


def mock_aop(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        pprint('[AOP]do aop before advice!')
        return f(*args, **kwargs)

    return wrapper


@mock_aop
def deco_func():
    pprint('simpson is coming!')


def run():
    deco_func()


if __name__ == '__main__':
    run()
