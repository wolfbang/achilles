#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : attribute_magic.py
# @Author: lucas
# @Date  : 9/4/18
# @Desc  :

from instance_init import Student
from class_init import Sample


class Assistant(Student):
    def __init__(self, id, name, score, title):
        super(Student, self).__init__()
        self.id = id
        self.title = title
        self.name = name
        self.score = score

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def access_attr():
    import random
    uid = random.randint(100, 1000)
    assistant = Assistant(uid, 'elon', 80, 'Assistant')
    for k in ['title', 'id', 'phone']:
        if hasattr(assistant, k):
            v = getattr(assistant, k)
            print v


def mock():
    anderson = Student('Bart Simpson', 90)
    print anderson

    import random
    uid = random.randint(100, 1000)
    assistant = Assistant(uid, 'elon', 80, 'Assistant')
    import pprint
    pprint.pprint(assistant)
    pprint.pprint(assistant.get_id())

    sample = Sample('Simpson', 25, 78, 2, 'TV series')
    print sample


def run():
    mock()
    access_attr()


if __name__ == '__main__':
    run()
