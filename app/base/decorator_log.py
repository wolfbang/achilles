#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_log.py
# @Author: lucas
# @Date  : 8/17/18
# @Desc  :


from functools import wraps
import pprint
import numpy as np


def log_it(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            log_string = '{func_name} is called'.format(func_name=func.__name__)

            with open(logfile, 'a') as file:
                file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrap_func

    return logging_decorator


@log_it()
def _func():
    random_num = np.random.randint(1000, 4000)
    pprint.pprint('{random_num}'.format(random_num=random_num))


@log_it('out2.log')
def _do_log():
    pass


def run():
    _func()
    _do_log()


if __name__ == '__main__':
    run()
