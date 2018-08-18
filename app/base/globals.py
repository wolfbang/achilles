#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : globals.py
# @Author: lucas
# @Date  : 8/18/18
# @Desc  :


import pprint


def add(x=1, y=3):
    result = x + y
    return result


def add2(x=2, y=4):
    global result
    result = x + y


def run():
    num = add(1, 5)
    pprint.pprint(num)


if __name__ == '__main__':
    run()
