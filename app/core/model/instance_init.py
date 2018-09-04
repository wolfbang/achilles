#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : instance_init.py
# @Author: lucas
# @Date  : 9/3/18
# @Desc  :


class Student(object):
    id = 0

    def __init__(self, name, score):
        super(Student, self).__init__()
        self.__name = name
        self.__score = score

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def print_score(self):
        print '%s,%s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif 70 < self.__score < 90:
            return 'B'
        elif self.__score > 60 and self.__score:
            return 'C'
        else:
            return 'D'

    def get_id(self):
        return self.id


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
    print student.get_grade()


if __name__ == '__main__':
    run()
