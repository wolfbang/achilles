#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : instance_init.py
# @Author: lucas
# @Date  : 9/3/18
# @Desc  :


class Student(object):
    def __init__(self, name, score):
        super(Student, self).__init__()
        self.name = name
        self.score = score

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def print_score(self):
        print '%s,%s' % (self.name, self.score)


def run():
    student = Student('lucas ley', score=80)
    print student

    student = Student('Elon Musk', score=75)
    print student
    import pprint
    pprint.pprint(student)
    student.print_score()
    pprint.pprint(str(student.__dict__))
    print str(student.__dict__)


if __name__ == '__main__':
    run()
