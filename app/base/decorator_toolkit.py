#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_toolkit.py
# @Author: lucas
# @Date  : 8/18/18
# @Desc  :


from functools import wraps
import pprint


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrap_fuction(*args, **kwargs):
            log_string = '{method_name} is called!'.format(method_name=__name__)
            pprint.pprint(log_string)

            with open(self.logfile, 'a') as log_file:
                log_file.write(log_string + '\n')

            self.notify()
            return func(*args, **kwargs)

        return wrap_fuction

    def notify(self):
        pprint.pprint('{func_name}'.format(func_name=__name__))
        pass


@logit()
def __func():
    pprint.pprint('__func is called')
    pass


def run():
    __func()


if __name__ == '__main__':
    run()
