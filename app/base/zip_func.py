#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zip_func.py
# @Author: lucas
# @Date  : 8/29/18
# @Desc  :


import pprint


def concate(list_a, list_b):
    return list_a + list_b


def _mock_concate():
    """mock list concatenate"""
    iter_a = [x for x in range(0, 10)]
    iter_b = [str(x) for x in range(10, 20)]
    concate_list = concate(iter_a, iter_b)
    pprint.pprint(concate_list)


def _mock_zip():
    list_a = [1, 2, 4]
    list_b = ['A', 'B', 'M', 'p', 'o', '7', 'Q']
    zipped_list = zip(list_a, list_b)
    pprint.pprint('result={result},type={_type}'.format(result=zipped_list, _type=type(zipped_list)))
    pprint.pprint(zip(*zipped_list))
    pprint.pprint(len(zipped_list))


def product(a, b):
    return a * b


def add(a, b):
    return a + b


def _func():
    bool_expression = False
    result = product if bool_expression else add
    pprint.pprint(type(result))
    pprint.pprint(result.__name__)


def run():
    _mock_zip()
    _mock_concate()
    _func()


if __name__ == '__main__':
    run()
