#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : member.py
# @Author: lucas
# @Date  : 9/4/18
# @Desc  :


class SchoolMember(object):
    """represents any school member"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)

    def tell(self):
        """tell the detail"""
        import pprint
        pprint.pprint('name:{name},age:{age}'.format(name=self.name, age=self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        import pprint
        pprint.pprint('Initialize Teacher name: {name}'.format(name=self.name))

    def __str__(self):
        return str(self.__dict__)

    def tell(self):
        SchoolMember.tell(self)
        import pprint
        pprint.pprint('Salary:{salary}'.format(salary=self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def __str__(self):
        return str(self.__dict__)

    def tell(self):
        SchoolMember.tell(self)
        import pprint
        pprint.pprint('Marks:{marks}'.format(marks=self.marks))


def mock():
    school_member = SchoolMember('Lucas', 18)
    teacher = Teacher('Mark', 28, 9000)
    student = Student('Nicholas', 18, 78)
    print school_member, teacher, student

    members = [school_member, teacher, student]
    for member in members:
        member.tell()


def run():
    mock()


if __name__ == '__main__':
    run()
