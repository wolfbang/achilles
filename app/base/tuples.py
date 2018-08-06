#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tuples.py
# @Author: lucas
# @Date  : 8/6/18
# @Desc  :


import pprint


def base():
    simple = (1, 2, 3, 4, 4)
    pprint.pprint(type(simple))
    pprint.pprint(simple)
    pprint.pprint('len: %s' % len(simple))


def init():
    magic_tuple = tuple((18, 2, 93, 4, 46))
    pprint.pprint(magic_tuple)
    pprint.pprint(magic_tuple[2])
    print tuple((18, 2, 93, 9000))


def run():
    base()
    init()


if __name__ == '__main__':
    run()
