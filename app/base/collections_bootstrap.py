#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : collections_bootstrap.py
# @Author: lucas
# @Date  : 8/5/18
# @Desc  :


def _info():
    print __name__
    return __name__


def init():
    data = {'first': {'micro': 'micro_value'}, 'middle': {}, 'last': {}}
    return data


def lookup(data, label, name):
    return data[label].get(name)


def _map():
    data = init()
    target = lookup(data, 'first', 'micro')
    print target


def _list():
    names = ['apple', 'spacex']
    ns = names[:]
    print type(ns), type(names)
    print ns, names
    print ns == names
    ns[0] = 'facebook'
    print ns, names


def run():
    _info()
    _list()
    _map()


if __name__ == '__main__':
    run()
