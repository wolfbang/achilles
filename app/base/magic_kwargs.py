#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : magic_kwargs.py
# @Author: lucas
# @Date  : 8/9/18
# @Desc  :


import pprint


def greet_me(**kwargs):
    for key, value in kwargs.items():
        pprint.pprint('{0} = {1}'.format(key, value))


def run():
    greet_me(name='lucas', gender='male', address='shanghai,china')
    greet_me(nickname='ll', skill='coding', signature='stay hungary,stay foolish')
    greet_me(major='computer science', hobby='honor of glory', company='google')


if __name__ == '__main__':
    run()
