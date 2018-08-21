#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mutable_immutable.py
# @Author: lucas
# @Date  : 8/19/18
# @Desc  :


import pprint


def __mutable():
    foo = ['hi']
    pprint.pprint(foo)
    bar = foo
    bar += ['ricardo']
    pprint.pprint(bar)
    pprint.pprint('{foo}'.format(foo=foo))


def add_to(num, target=None):
    if not target:
        target = []
    target.append(num)
    return target


def run():
    __mutable()
    result = add_to(1)
    pprint.pprint('{result}'.format(result=result))
    target = [1, 2, 3]
    result = add_to(5, target=target)
    pprint.pprint(result)


if __name__ == '__main__':
    run()
