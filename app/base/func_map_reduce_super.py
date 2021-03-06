#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : func_map_reduce_super.py
# @Author: lucas
# @Date  : 8/27/18
# @Desc  :


import pprint


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def _mock():
    str_input = '14689'
    result = reduce(fn, map(char2num, str_input))
    pprint.pprint(result)

    result = str2int('9876')
    pprint.pprint('result={result},type={raw_type}'.format(result=result, raw_type=type(result)))


def run():
    _mock()


if __name__ == '__main__':
    run()
