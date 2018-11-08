#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lambda_func.py
# @Author: lucas
# @Date  : 11/8/18
# @Desc  :

from pprint import pprint


def add():
    return lambda x, y: x + y


def mock_lambda():
    adder = add()
    pprint(adder(23, 678))


def mock_sort():
    number_pairs = [(10, 4), (17, 2), (1, 12), (-1, 56), (45, 87), (80, 9)]
    pprint(number_pairs)
    number_pairs.sort(key=lambda item: item[1])
    pprint(number_pairs)


def mock_zip():
    list_1 = [1, 90, 5, 6, 97, 37, 123]
    list_2 = [3, 6, 5, 16, 57, 47, 8]
    data = zip(list_1, list_2)
    pprint(data)

    list_1, list_2 = map(lambda t: list(t), zip(*data))
    pprint((list_1, list_2))


def run():
    mock_lambda()
    mock_sort()
    mock_zip()


if __name__ == '__main__':
    run()
