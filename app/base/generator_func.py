#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : generator_func.py
# @Author: lucas
# @Date  : 8/22/18
# @Desc  :


import pprint


def __mock_yield():
    yield 1
    yield 2
    yield 3


def __mock_yield_with():
    pprint.pprint('{func} block'.format(func='__mock_yield_with'))
    yield 1
    while False:
        yield 2

    yield 3


def __mock():
    yield_generator = __mock_yield()
    for item in yield_generator:
        pprint.pprint(item)

    yield_generator = __mock_yield_with()
    for item in yield_generator:
        pprint.pprint(item)


def __func_send():
    number = 1
    while True:
        number *= 2
        yield number
        if number > 10:
            break


def __run_func_send():
    generator = __func_send()
    for item in generator:
        pprint.pprint(item)


def run():
    __mock()
    __run_func_send()


if __name__ == '__main__':
    run()
