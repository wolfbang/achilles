#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : filter_magic.py
# @Author: lucas
# @Date  : 8/28/18
# @Desc  :

import pprint
import os


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and str(s).strip()


def _filter():
    numbers = list(filter(is_odd, [x for x in range(0, 100)]))
    pprint.pprint(numbers)

    string_container = ['a', '', 'A', None, 'AF']
    not_empty_strings = list(filter(not_empty, string_container))
    pprint.pprint('original_size:{original_size},filtered_size:{filtered_size},before={before},after={after}'.format(
        original_size=len(string_container), filtered_size=len(not_empty_strings), before=string_container,
        after=not_empty_strings))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


def _find_primes():
    for n in primes():
        if n < 100:
            pprint.pprint('prime:{prime}'.format(prime=n))
        else:
            break


def run():
    _filter()
    # _find_primes()


if __name__ == '__main__':
    run()
