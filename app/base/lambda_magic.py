#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lambda_magic.py
# @Author: lucas
# @Date  : 8/29/18
# @Desc  :

import pprint


def add_with_lambda(x, y):
    adder = lambda a, b: a + b
    return adder(x, y)


def _mock_map():
    seq = [1, 2, 3, 4, 4]

    sum_result = reduce(lambda x, y: x + y, seq)
    pprint.pprint('[REDUCE]sum is {sum_result}'.format(sum_result=sum_result))

    sum_result = sum(map(int, seq))
    pprint.pprint('[MAP]sum is {sum_result}'.format(sum_result=sum_result))


def _mock_lambda():
    result = add_with_lambda(1, 98)
    pprint.pprint(result)


def run():
    _mock_lambda()
    _mock_map()


if __name__ == '__main__':
    run()
