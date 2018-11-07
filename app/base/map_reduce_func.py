#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : map_reduce_func.py
# @Author: lucas
# @Date  : 11/7/18
# @Desc  :

from pprint import pprint


def power(number):
    return number * number


def map_power():
    items = [1, 2, 5, 6, 7]
    squred = list(map(power, items))
    pprint(squred)


def map_lambda():
    items = [1, 3, 5, 7, 9]
    squared = list(map(lambda x: x * x, items))
    pprint(squared)


def multiply(x):
    return x * x


def add(x):
    return x + x


def great_func():
    funcs = [multiply, add]
    for i in range(5):
        value = list(map(lambda x: x(i), funcs))
        pprint(value)


def run():
    map_power()
    map_lambda()
    great_func()


if __name__ == '__main__':
    run()
