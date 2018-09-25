#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_less_than_ten.py
# @Author: lucas
# @Date  : 9/25/18
# @Desc  :

from pprint import pprint


def get_target_numbers(numbers, min_num):
    if not isinstance(numbers, list):
        raise Exception('only list is accepted!')

    if not min_num:
        raise Exception('min_num can not be null!')

    if not isinstance(min_num, int):
        raise Exception('min_num should be integer!')

    return [x for x in numbers if x >= min_num]


def mock():
    numbers = [1, 4, 4, 5, 34, 26, 89, 99]
    less_than_ten = [x for x in numbers if x > 10]
    pprint(less_than_ten)

    less_than_ten = get_target_numbers(numbers=numbers, min_num=10)
    pprint(less_than_ten)
    get_target_numbers(numbers, 12)


def run():
    mock()


if __name__ == '__main__':
    run()
