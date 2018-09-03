#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : partial_func.py
# @Author: lucas
# @Date  : 9/3/18
# @Desc  :


import pprint
import functools


def _int2_with_partial(x):
    int2_func = functools.partial(int, base=2)
    return int2_func(x)


def int2(x):
    return int(x, base=2)


def run():
    x = int2('01010101')
    pprint.pprint(x)
    x = _int2_with_partial('01010101')
    pprint.pprint(x)


if __name__ == '__main__':
    run()
