#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : func_map_reduce.py
# @Author: lucas
# @Date  : 8/27/18
# @Desc  :


import pprint


def f(x):
    return x * x


def _map():
    result = map(f, [1, 2, 4, 5])
    pprint.pprint(list(result))
    str_list = map(str, result)
    pprint.pprint('str_list={str_list}'.format(str_list=str_list))


def fn(x, y):
    return x * 10 + y


def _reduce():
    init = [1, 2, 6, 9]
    result = reduce(fn, init)
    pprint.pprint('result:{result}'.format(result=result))


def run():
    _map()
    _reduce()


if __name__ == '__main__':
    run()
