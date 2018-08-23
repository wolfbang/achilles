#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : generator_magic.py
# @Author: lucas
# @Date  : 8/22/18
# @Desc  :

import pprint


class Bank(object):
    crisis = False

    def __init__(self):
        super(Bank, self).__init__()

    def create_atm(self):
        while not self.crisis:
            yield "$100"


def __mock():
    hsbc = Bank()
    google_atm = hsbc.create_atm()
    pprint.pprint(google_atm.next())
    pprint.pprint(google_atm.next())
    return google_atm


def __mock_withdraw():
    actions = [__mock().next() for case in range(5)]
    pprint.pprint(actions)


def __generator():
    numbers = [x for x in range(1, 10)]
    for num in numbers:
        yield num * num


def __test():
    instance = __generator()
    for i in instance:
        pprint.pprint(i)


def run():
    instance = __generator()
    pprint.pprint(instance)
    __test()
    __mock()
    __mock_withdraw()


if __name__ == '__main__':
    run()
