#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorate_class.py
# @Author: lucas
# @Date  : 8/16/18
# @Desc  :


import pprint
from functools import wraps


def p_decorate(func):
    @wraps(func)
    def wrap_func(self):
        pprint.pprint('[Wrap Printer]{0}'.format(func(self)))
        return '{0}'.format(func(self))

    return wrap_func


def pp_decorate(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        pprint.pprint('[Wrap Printer pp_decorate] {0}'.format(func(*args, **kwargs)))
        return '{0}'.format(func(*args, **kwargs))

    return func_wrapper


class Gender():
    male = 1
    female = 2


class Person(object):
    def __init__(self):
        self.id = 1L
        self.name = 'lucas'
        self.family = 'Ley'

    @pp_decorate
    def get_fullname(self):
        return self.name + " " + self.family


def run():
    person = Person()
    person.get_fullname()


if __name__ == '__main__':
    run()
