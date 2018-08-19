#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : person.py
# @Author: lucas
# @Date  : 8/17/18
# @Desc  :


import datetime
import pprint


class Person(object):
    """
    person class
    """

    """init class object"""
    def __init__(self):
        self.id = 1
        self.nickname = 'mark'
        self.address = 'shanghai,china'
        self.birthday = datetime.datetime.now()

    """__str__ > __repr__"""
    def __repr__(self):
        return str(self.__dict__)

    """called when use print"""
    def __str__(self):
        return super(Person, self).__str__()

    def __hash__(self):
        return super(Person, self).__hash__()

    def __ne__(self, o):
        return super(Person, self).__ne__(o)

    """set attribute"""
    def __setattr__(self, name, value):
        super(Person, self).__setattr__(name, value)

    """delete attribute"""
    def __delattr__(self, name):
        super(Person, self).__delattr__(name)

    """is equal to another object"""
    def __eq__(self, o):
        return super(Person, self).__eq__(o)

    """get attribute"""
    def __getattribute__(self, name):
        return super(Person, self).__getattribute__(name)

    def __reduce__(self):
        return super(Person, self).__reduce__()

    """create new instance"""
    def __new__(cls):
        return super(Person, cls).__new__(cls)

    def __format__(self, format_spec):
        return super(Person, self).__format__(format_spec)

    def __reduce_ex__(self, protocol):
        return super(Person, self).__reduce_ex__(protocol)

    """size of object"""
    def __sizeof__(self):
        return super(Person, self).__sizeof__()


def run():
    person = Person()
    pprint.pprint(person)


if __name__ == '__main__':
    run()
