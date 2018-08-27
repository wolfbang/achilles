#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : func_magic.py
# @Author: lucas
# @Date  : 8/27/18
# @Desc  :

import pprint


def add(a, b, func):
    return func(a) + func(b)


def _mock():
    result = add(1, -90, func=abs)
    pprint.pprint(result)

    result = add(5, 120, abs)
    pprint.pprint(result)


def run():
    _mock()


if __name__ == '__main__':
    run()
