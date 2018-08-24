#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yield_func.py
# @Author: lucas
# @Date  : 8/22/18
# @Desc  :


def __generate():
    i = 0
    while True:
        m = yield i
        print 'yield i=', type(m)

        print "m = ", m
        i += 1  #
        if i > 100:
            break


def func():
    x = 1
    while True:
        y = (yield x)
        x += y


def run():
    g = __generate()
    g.next()
    g.send(5)

    generator = func()
    print generator.next()  # 1
    print generator.send(3)  # 4
    print generator.send(10)  # 14


if __name__ == '__main__':
    run()
