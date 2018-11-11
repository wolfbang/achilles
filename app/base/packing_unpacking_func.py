#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : packing_unpacking_func.py
# @Author: lucas
# @Date  : 11/11/18
# @Desc  :

from pprint import pprint


def func(*args, **kwargs):
    pprint('Arguments:%s' % (args,))
    pprint('KeyValue Arguments:%s ' % kwargs)


def repeat(count, name):
    for index in range(count):
        pprint(name)


def run():
    args = [4, 'beer']
    repeat(*args)

    pprint('Unpacking with kwargs')
    kwargs = {'count': 4, 'name': 'beer'}
    repeat(**kwargs)

    pprint('Keyword Arguments:')
    func(4, 'simpson', 'pandora', key='some key', sort='pipe')


if __name__ == '__main__':
    run()
