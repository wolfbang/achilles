#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : regular_expressions.py
# @Author: lucas
# @Date  : 8/7/18
# @Desc  :


import re


def _regular():
    string = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', string)
    if match:
        print 'Found', match.group()
    else:
        print 'Not Found'


def run():
    _regular()


if __name__ == '__main__':
    run()
