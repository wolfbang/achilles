#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yield_mock.py
# @Author: lucas
# @Date  : 8/24/18
# @Desc  :

import pprint


def __consumer():
    r = 'yield'
    while True:
        n = yield r
        if not n:
            return

        pprint.pprint('[Consumer] consuming {value}'.format(value=n))
        r = '200 ok'


def __producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        pprint.pprint('[PRODUCER] producing {value}'.format(value=n))
        r = c.send(n)
        pprint.pprint('[Producer] consumer return:%s' % r)

    c.close()


def __mock():
    consumer = __consumer()
    __producer(consumer)


def run():
    __mock()


if __name__ == '__main__':
    run()
