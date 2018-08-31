#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_func.py
# @Author: lucas
# @Date  : 8/30/18
# @Desc  :

import pprint
from random import randint


def _mock_sort():
    seq = [randint(-100, 100) for x in range(0, 10)]
    pprint.pprint(seq)
    seq_sorted = sorted(seq)
    pprint.pprint(seq_sorted)

    seq_sorted = sorted(seq, key=abs)
    pprint.pprint(seq_sorted)


def _mock_sort_string():
    seq = ['Bob', 'Alice', 'Lucas', 'Matt', 'Billy']
    seq_sorted = sorted(seq, key=str.lower)
    pprint.pprint(seq_sorted)
    seq_sorted_reverse = sorted(seq, key=str.lower, reverse=True)
    pprint.pprint(seq_sorted_reverse)


def by_name(t):
    return tuple(t)[0]


def by_score(t):
    return tuple(t)[1]


def _mock_sort_by_name():
    """sort test"""
    original = [('Bob', 76), ('Matt', 70), ('Joe', 60), ('Alice', 80), ('Dan', 90)]
    pprint.pprint(sorted(original, key=by_name))
    pprint.pprint(sorted(original, key=lambda x: x[1]))  # by score,default asc
    pprint.pprint(sorted(original, key=lambda x: x[0], reverse=False))  # by name desc
    pprint.pprint(sorted(original, key=by_score))


def run():
    _mock_sort()
    _mock_sort_string()
    _mock_sort_by_name()


if __name__ == '__main__':
    run()
