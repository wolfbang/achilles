#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : set_magic.py
# @Author: lucas
# @Date  : 9/24/18
# @Desc  :


from pprint import pprint


def base():
    unique = {1, 2, 4, 5, 5, 6}
    pprint(unique)
    pprint(type(unique))
    unique_mutation = set([1, 25, 6, 7, 7, 7, 9])
    pprint(unique_mutation)
    pprint(unique.union(unique_mutation))
    pprint(unique.difference(unique_mutation))
    pprint(unique.intersection(unique_mutation))
    pprint(unique.copy() is unique)
    pprint(unique.symmetric_difference(unique_mutation))


def run():
    base()


if __name__ == '__main__':
    run()
