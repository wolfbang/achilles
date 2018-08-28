#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : filter_power.py
# @Author: lucas
# @Date  : 8/29/18
# @Desc  :


import pprint


def _not_black(s):
    return s and str(s).strip()


def _mock(alphabet, iter_container):
    if not iter_container:
        return False

    if alphabet in iter_container:
        return True

    return False


def _filter(iter):
    return filter(_not_black, iter)


def run():
    alphabets = ['a', 'G', 'b', 'x', 'U', '', 'e', 'Q', 'F', None]
    pprint.pprint(_mock('G', alphabets))
    pprint.pprint(_filter(alphabets))


if __name__ == '__main__':
    run()
