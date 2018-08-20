#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : introspections.py
# @Author: lucas
# @Date  : 8/20/18
# @Desc  :


import pprint


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


def run():
    __init()
    __type()


if __name__ == '__main__':
    run()
