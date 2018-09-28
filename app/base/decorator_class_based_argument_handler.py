#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_class_based_argument_handler.py
# @Author: lucas
# @Date  : 9/28/18
# @Desc  :


from functools import wraps
from pprint import pprint


class ClassBaseArgsDecorator(object):
    def __init__(self, arg1, arg2):
        pprint('INIT ClassBaseArgsDecorator')
        self.arg1 = arg1
        self.arg2 = arg2
        pprint('[init]args %s,%s' % (arg1, arg2))

    def __call__(self, func):
        pprint('CALL ClassBaseArgsDecorator.Congratulations!')
        # pprint('[CALL args] %s,%s' % (args, kwargs))

        @wraps(func)
        def new_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return new_func


@ClassBaseArgsDecorator('parameter1', 'parameter2')
def print_args_again(*args):
    for arg in args:
        pprint(arg)


def run():
    print_args_again('X', 'Y', 'Z')
    print_args_again(1, 2, 5)


if __name__ == '__main__':
    run()
