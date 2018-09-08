#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pickle_magic.py
# @Author: lucas
# @Date  : 9/6/18
# @Desc  :


import pickle


class People(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.__dict__)


def mock():
    p = People('John')
    path = '/Users/lucas/projects/achilles/app/base/person.txt'
    with open(path, 'wb') as txt_file:
        pickle.dump(p, txt_file, 0)

    with open(path, 'rb') as txt_file:
        pp = pickle.load(txt_file)
        print pp


def run():
    mock()


if __name__ == '__main__':
    run()
