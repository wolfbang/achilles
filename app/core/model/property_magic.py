#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : property_magic.py
# @Author: lucas
# @Date  : 9/10/18
# @Desc  :


class Student(object):
    def __str__(self):
        return str(self.__dict__)

    @property
    def birth(self):
        return self.birthday

    @birth.setter
    def birth(self, value):
        self.birthday = value

    @property
    def age(self):
        return 2018 - self.birth


def run():
    student = Student()
    student.birth = 1990
    print student, student.age


if __name__ == '__main__':
    run()
