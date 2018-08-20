#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : return_pair.py
# @Author: lucas
# @Date  : 8/19/18
# @Desc  :


import pprint


def __return_with_tuple():
    _name = 'elon'
    _age = 28
    return (_name, _age)


def __init_profile():
    global name
    global age

    name = 'paulinho'
    age = 28

    return name, age


def run():
    info = __init_profile()
    pprint.pprint('{info}'.format(info=info))
    pprint.pprint('{name},{age}'.format(name=name, age=age))
    info = __return_with_tuple()
    pprint.pprint(info)


if __name__ == '__main__':
    run()
