#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yield_magic.py
# @Author: lucas
# @Date  : 8/22/18
# @Desc  :


import pprint


def _mock(number=10):
    while True:
        x = yield number
        x *= 2
        pprint.pprint('{num}'.format(num=x))


def run():
    _generator = _mock(1)
    number = _generator.next()
    number = _generator.send(20)
    number = _generator.send(100)
    pprint.pprint(number)


if __name__ == '__main__':
    run()
