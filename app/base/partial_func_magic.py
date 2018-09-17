#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : partial_func_magic.py
# @Author: lucas
# @Date  : 9/17/18
# @Desc  :


from pprint import pprint
import functools


def f(a, b=3):
    return a + b


def run():
    f2 = functools.partial(f, 1)
    pprint(f2(9))
    pprint(f2())

    f3 = functools.partial(f, b=10)
    pprint(f3(1))
    pprint(f3(6))


if __name__ == '__main__':
    run()
