#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : comprehensions.py
# @Author: lucas
# @Date  : 8/10/18
# @Desc  :


import pprint
import random


def _list_comprehension():
    numbers = [x for x in range(1, 10) if x % 2 is 0]
    pprint.pprint(numbers)
    return numbers


def _set_comprehension():
    members = {random.randint(50, 100) for x in range(1, 10) if x % 1 is 0}
    pprint.pprint(members)
    squared = {x ** 2 for x in range(0, 10)}
    pprint.pprint(squared)


def _map_comprehension():
    dictionary_map = {'G': 'Gone', 'P': 'Python', 'J': 'Java'}
    pprint.pprint(dictionary_map)

    dict_case = {
        k.lower(): '{0}-{1}'.format(dictionary_map.get(k.lower(), 'LowerDefault'),
                                    dictionary_map.get(k.upper(), 'UpperDefault'))
        for k in dictionary_map.keys()
    }

    pprint.pprint(dict_case)

    swap_dict = {v: k for k, v in dictionary_map.items()}
    pprint.pprint('[Result {0}]'.format(swap_dict))


def run():
    _list_comprehension()
    _set_comprehension()
    _map_comprehension()


if __name__ == '__main__':
    run()
