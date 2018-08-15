#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : function_power.py
# @Author: lucas
# @Date  : 8/15/18
# @Desc  :


import pprint


def do_hi(name='lucas'):
    pprint.pprint('inside the do_hi() function now!')

    def greet():
        return 'inside the greet() function!'

    def welcome():
        return 'inside the welcome() function!'

    pprint.pprint(greet())
    pprint.pprint(welcome())

    pprint.pprint('now back in the do_hi() function')

    if name == 'lucas':
        return greet

    else:
        return welcome


def _do_sth_before_hi(func):
    pprint.pprint('I\'m doing some boring work before executing hi() ')
    pprint.pprint(func())


def run():
    hi = do_hi()
    pprint.pprint('[run] {0}'.format(hi))
    pprint.pprint('[run] {0}'.format(hi()))
    _do_sth_before_hi(hi)


if __name__ == '__main__':
    run()
