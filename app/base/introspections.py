#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : introspections.py
# @Author: lucas
# @Date  : 8/20/18
# @Desc  :


import pprint
import inspect


def __init():
    numbers = [x for x in range(1, 10)]
    introspection = dir(numbers)
    pprint.pprint(introspection)


def __type():
    pprint.pprint(type(''))
    pprint.pprint(type({}))
    pprint.pprint(type([]))
    pprint.pprint(type((1, 2)))
    pprint.pprint(type(5))
    pprint.pprint(id('google'))


def __introspection():
    pprint.pprint(inspect.getmembers([x for x in range(1, 10)]))


def run():
    __init()
    __type()
    __introspection()


if __name__ == '__main__':
    run()
