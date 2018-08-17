#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : randoms.py
# @Author: lucas
# @Date  : 8/9/18
# @Desc  :


import random
import numpy as np
import pprint


def _numpy_random():
    random_number = np.random.random_integers(0, 100)
    pprint.pprint(random_number)
    result = np.random.randint(1041389120000,1041389120001)
    print result


def run():
    values = list(range(0, 100))
    random_value = random.choice(values)
    pprint.pprint(random_value)
    _numpy_random()


if __name__ == '__main__':
    run()
