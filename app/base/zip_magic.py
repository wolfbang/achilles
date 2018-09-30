#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zip_magic.py
# @Author: lucas
# @Date  : 9/30/18
# @Desc  :

from pprint import pprint


def base():
    keys = ['x', 'y', 'z', 'p', 'J']
    vals = [1, 2, 5, 6]
    kw_tuple = zip(keys, vals)
    for item in kw_tuple:
        pprint(type(item))
    pprint(type(kw_tuple))
    kw_dict = dict(kw_tuple)
    pprint(type(kw_dict))
    pprint(kw_dict)


def run():
    base()


if __name__ == '__main__':
    run()
