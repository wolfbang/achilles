#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : password_generator.py
# @Author: lucas
# @Date  : 9/12/18
# @Desc  :

import random
import string
from pprint import pprint


def random_char():
    return random.choice(string.letters + string.digits)


def password_generator(length):
    if not length:
        raise ValueError('length can not be None!')
    if not isinstance(length, int):
        raise ValueError('length should be integer!')
    if length <= 0:
        raise ValueError('length should be greater than 0')
    random_chars = ''.join(random_char() for x in xrange(length))
    return random_chars


def run():
    pprint(password_generator(1))
    pprint(password_generator(10))
    pprint(password_generator(16))


if __name__ == '__main__':
    run()
