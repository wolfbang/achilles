#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_do_retry.py
# @Author: lucas
# @Date  : 10/3/18
# @Desc  :

from functools import wraps
from pprint import pprint
from time import sleep

import logging

logging.basicConfig()
logger = logging.getLogger('retry')


def retry(time=3):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for x in range(0, time):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    sleep(1)
                    logging.error('Exception:%s' % e)

        return wrapper

    return deco


counter = 0


@retry()
def save_to_db(arg):
    pprint('[Save] do save now!')

    global counter
    counter += 1
    if counter < 3:
        raise ValueError('value error %s' % arg)

    pprint('No error now and Done!')


def run():
    save_to_db('save to facebook!')


if __name__ == '__main__':
    run()
