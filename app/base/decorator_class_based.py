#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_class_based.py
# @Author: lucas
# @Date  : 9/27/18
# @Desc  :


import functools
from pprint import pprint


class ClassBaseDecorator(object):
    def __init__(self, func_to_decorate):
        pprint('Init ClassBaseDecorator')
        self.func_to_decorate = func_to_decorate

    def __call__(self, *args, **kwargs):
        pprint("CALL ClassBaseDecorator")
        self.func_to_decorate(*args, **kwargs)


@ClassBaseDecorator
def print_moar_args(*args):
    pprint(type(args))
    pprint('do something,args %s' % (args,))
    for arg in args:
        pprint(arg)


def run():
    print_moar_args('X', 'Y', 'Z')


if __name__ == '__main__':
    run()
