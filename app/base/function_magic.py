#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : function_magic.py
# @Author: lucas
# @Date  : 8/15/18
# @Desc  :


import pprint


def hi(name='yasoob'):
    return 'hi ' + name


def _test_hi():
    greeting = hi
    pprint.pprint(greeting('robot_function'))

    # del hi
    # pprint.pprint(hi())

    pprint.pprint(greeting())


def run():
    pprint.pprint(hi())
    pprint.pprint(hi('taliska'))
    _test_hi()


if __name__ == '__main__':
    run()
