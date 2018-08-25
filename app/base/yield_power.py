#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yield_power.py
# @Author: lucas
# @Date  : 8/25/18
# @Desc  :


import pprint


def foo():
    while True:
        x = yield
        pprint.pprint('{x}'.format(x=x))


def __mock():
    g = foo()
    g.next()
    g.send(1)
    g.send(2)
    g.next()


def deco(func):
    def wrapper():
        res = func()
        next(res)
        return res

    return wrapper


@deco
def foo2():
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        pprint.pprint('food in food list are {food_list}'.format(food_list=food_list))


def __mock_food():
    g = foo2()
    pprint.pprint('result = {result}'.format(result=g.send('apple')))
    pprint.pprint(g.send('pear'))
    pprint.pprint(g.send('watermelon'))


def run():
    __mock()
    __mock_food()


if __name__ == '__main__':
    run()
