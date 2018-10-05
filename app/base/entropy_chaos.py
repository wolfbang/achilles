#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : entropy_chaos.py
# @Author: lucas
# @Date  : 10/5/18
# @Desc  :


from pprint import pprint


def entropy():
    factor = float(raw_input('please enter a number between 0 and 1: '))
    for f in range(10):
        factor = 3.9 * factor * (1 - factor)
        pprint(factor)


def run():
    entropy()


if __name__ == '__main__':
    run()
