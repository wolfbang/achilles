#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : attribute_magic.py
# @Author: lucas
# @Date  : 9/4/18
# @Desc  :

from instance_init import Student


class Assistant(Student):
    def __init__(self, name, score, title):
        super(Student, self).__init__()
        self.title = title

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def mock():
    anderson = Student('Bart Simpson', 90)
    print anderson
    assistant = Assistant('elon', 80, 'Assistant')
    import pprint
    pprint.pprint(assistant)
    pprint.pprint(assistant.get_id())


def run():
    mock()


if __name__ == '__main__':
    run()
