#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : yield_deco.py
# @Author: lucas
# @Date  : 8/27/18
# @Desc  :

import os
import sys
import pprint

reload(sys)
sys.setdefaultencoding('utf8')


def deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res

    return wrapper


@deco
def search(target):
    while True:
        path = yield
        g = os.walk(path)
        for par_dir, _, files in g:
            for f in files:
                file_path = r'%s/%s' % (par_dir, f)
                target.send(file_path)


@deco
def opener(target):
    while True:
        file_path = yield
        with open(file_path) as f:
            target.send((target, f))


@deco
def cat(target):
    while True:
        file_path, f = yield
        for line in f:
            tag = target.send((file_path, line))
            if tag:
                break


@deco
def grep(target, pattern):
    tag = False
    while True:
        file_path, line = yield tag
        tag = False
        if pattern in line:
            target.send(file_path)
            tag = True


@deco
def printer():
    while True:
        file_name = yield
        pprint.pprint(file_name)


def run():
    path = '/Users/lucas/projects/achilles'
    search(opener(cat(grep(printer(), 'reload')))).send(path)


if __name__ == '__main__':
    run()
