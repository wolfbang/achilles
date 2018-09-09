#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : class_slots.py
# @Author: lucas
# @Date  : 9/9/18
# @Desc  :


class Student(object):
    # __slots__ = ('name', 'address', 'phone_number')

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return str(self.__dict__)


def set_score(self, score):
    self.score = score


def run():
    student = Student('Simpson', 'L.A.,USA')
    Student.set_score = set_score
    print dir(student)
    print student
    student.set_score(80)
    print student


if __name__ == '__main__':
    run()
