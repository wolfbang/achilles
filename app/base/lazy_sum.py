#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lazy_sum.py
# @Author: lucas
# @Date  : 9/1/18
# @Desc  :


import pprint


def calc_sum(*args):
    ax = 0
    for x in args:
        ax += x
    return ax


def lazy_sum(*args):
    def custom_sum():
        ax = 0
        for x in args:
            ax += x
        return ax

    return custom_sum


def run():
    f = lazy_sum(1, 2, 4, 5)
    pprint.pprint(f())

    fn = lazy_sum(1, 343, 56, 1)
    pprint.pprint(fn())

    cal_sum = lazy_sum(1, 2, 90)
    pprint.pprint(cal_sum())


if __name__ == '__main__':
    run()
