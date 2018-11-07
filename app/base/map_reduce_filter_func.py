#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : map_reduce_filter_func.py
# @Author: lucas
# @Date  : 11/7/18
# @Desc  :


from pprint import pprint
from functools import reduce
import random


def do_filter():
    items = [random.randint(-100, 200) for item in range(10)]
    pprint(items)

    less_than_zero = list(filter(lambda x: x < 0, items))
    pprint(less_than_zero)

    greater_than_zero = list(filter(lambda x: x > 0, items))
    pprint(greater_than_zero)


def do_reduce():
    items = [random.randint(-100, 200) for item in range(10)]
    produce = reduce(lambda x, y: x + y, items)
    pprint(produce)

    produce = reduce(lambda x, y: x * y, [1, 2, 3, 4])
    pprint(produce)


def run():
    do_filter()
    do_reduce()


if __name__ == '__main__':
    run()
