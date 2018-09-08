#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pickle_file.py
# @Author: lucas
# @Date  : 9/7/18
# @Desc  :


import pickle
from app.core.model.robot import Robot


def mock():
    path = 'EMP.pickle'
    emp = {
        'name': 'More',
        'age': '28',
        'address': 'shanghai,china'
    }
    with open(path, 'wb') as pickle_file:
        pickle.dump(emp, pickle_file)

    with open(path, 'rb') as pickle_file:
        emp = pickle.load(pickle_file)
        print emp


def pickle_in_memory():
    robot = Robot('Bart Simpson')
    m = pickle.dumps(robot)
    print m
    robot = pickle.loads(m)
    print robot


def run():
    mock()
    pickle_in_memory()


if __name__ == '__main__':
    run()
