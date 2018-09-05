#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : class_init.py
# @Author: lucas
# @Date  : 9/5/18
# @Desc  :


class People(object):
    name = ''
    age = 0
    __weight = 0

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        import pprint
        pprint.pprint('{name} is speaking, I\'m {age} year(s) old! '.format(name=self.name, age=self.age))

    def __str__(self):
        return str(self.__dict__)


class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        import pprint
        pprint.pprint(
            'I\'m {name}, {age} year(s) old, and I\'m grade {grade}! glad to meet you all'.format(name=self.name,
                                                                                                  age=self.age,
                                                                                                  grade=self.grade))

    def __str__(self):
        return str(self.__dict__)


class Speaker(object):
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        import pprint
        pprint.pprint('hello,I\'m {name},my topic is {topic}'.format(name=self.name, topic=self.topic))

    def __str__(self):
        return str(self.__dict__)


class Sample(Speaker, Student):
    a = ''

    def __init__(self, name, age, weight, grade, topic):
        Speaker.__init__(self, name=name, topic=topic)
        Student.__init__(self, name=name, age=age, weight=weight, grade=grade)

    def __str__(self):
        return str(self.__dict__)


def mock():
    people = People('Joe', 20, 80)
    print people
    people.speak()

    random_people = People('Luke', 23, 78)
    print random_people

    student = Student('Ken', 23, 70, 3)
    print student
    student.speak()

    sample = Sample('Sam', 20, 67, 3, 'Science')
    print sample
    sample.speak()


def run():
    mock()


if __name__ == '__main__':
    run()
