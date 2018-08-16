#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_patch.py
# @Author: lucas
# @Date  : 8/16/18
# @Desc  :


import pprint
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrap_the_function():
        pprint.pprint('I\'m doing some boring work before executing a_func()')
        a_func()

        pprint.pprint('I\'m doing some boring work after executing a_func()')

    return wrap_the_function


def a_function_need_decoration():
    pprint.pprint('I\' a function need to be decorated to remove my ')


@a_new_decorator
def a_func_with_decorator():
    pprint.pprint('a_func_with_decorator execute!')


def p_decorate(func):
    @wraps(func)
    def func_wrapper(name):
        pprint.pprint('{0}'.format(func(name)))
        return '{0}'.format(func(name))

    return func_wrapper


@p_decorate
def get_text(name='Fort'):
    pprint.pprint('[func ]get_text starts! %s' % name)
    return 'hey %s ,go to bar!' % name


def run():
    a_new_decorator(a_function_need_decoration)
    pprint.pprint(a_function_need_decoration.__name__)
    a_func_with_decorator()
    get_text('christiano')


if __name__ == '__main__':
    run()
