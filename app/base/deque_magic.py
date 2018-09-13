#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : deque_magic.py
# @Author: lucas
# @Date  : 9/13/18
# @Desc  :


from pprint import pprint
from collections import deque
import os


def mock():
    d = deque('counting stars')
    for elem in d:
        pprint(elem.upper())

    d.append('!')
    pprint(d)

    d.appendleft("let's ")
    pprint(d)

    d.pop()
    pprint(d)

    d.popleft()
    pprint(d)

    pprint(list(d))
    pprint(list(reversed(d)))

    d.extend('! go go go !')
    pprint(d)

    d.rotate(-1)
    pprint(d)
    d.rotate(1)
    pprint(d)
    d.clear()


def tail(filename='', n=10):
    if not os.path.exists(filename):
        return
    return deque(open(filename, 'rb'), n)


def run():
    mock()
    pprint(tail('/Users/lucas/Downloads/hamlet.txt'))

    text = tail('')
    pprint(text)


if __name__ == '__main__':
    run()
