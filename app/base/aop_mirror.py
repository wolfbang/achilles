#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aop_mirror.py
# @Author: lucas
# @Date  : 9/18/18
# @Desc  :

from aop_func import aspectize, before, after
from pprint import pprint


@aspectize
class HandleClass(object):
    def __init__(self):
        self.x = 5

    def incr(self):
        pprint(self.x)
        return self.x


@before(HandleClass.incr)
def increase_x(self):
    self.x += 1


@after(HandleClass.incr)
def log_func(res):
    pprint('[Return] {}'.format(str(res)))


def run():
    c = HandleClass()
    c.incr()
    pprint(c)


if __name__ == '__main__':
    run()
