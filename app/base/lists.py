#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lists.py
# @Author: lucas
# @Date  : 8/5/18
# @Desc  :


import pprint
import random

ants = []


def ant():
    ants = [1, 2, 3, 4, 8]
    return ants


def base():
    elements = ant()
    print elements
    print 'list:', list(elements)
    print list('tensorflow')


def operation():
    elements = [1, 1, 1]
    print '[Before]', elements
    elements[1] = 2
    print elements
    del elements[2]
    print elements


def do_slice():
    names = list('tensorflow')
    print names
    names[2:] = list('Perl')
    print names
    print names[1:4]


def all_list():
    numbers = [1, 2, 3]
    print len(numbers)
    numbers.append(random.random())
    print numbers


def extend():
    numbers = [1, 3, 6]
    numbers2 = [4, 5, 6]
    numbers.extend(numbers2)
    print numbers
    print len(numbers)
    numbers.insert(4, random.random())
    print numbers
    head = numbers.pop()
    print '[head]', head
    numbers.remove(6)
    print numbers
    numbers.reverse()
    print numbers
    copy = numbers[:]
    copy.sort()
    print '[Sort]', copy


def list_comprehension():
    numbers = [1, 2, 3, 4]
    squares = [n * n for n in numbers]
    pprint.pprint(squares)
    squares = [n * n for n in numbers if n % 2 == 0]
    pprint.pprint(squares)


def run():
    base()
    operation()
    do_slice()
    all_list()
    extend()
    list_comprehension()


if __name__ == '__main__':
    run()
