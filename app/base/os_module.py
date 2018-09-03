#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : os_module.py
# @Author: lucas
# @Date  : 9/3/18
# @Desc  :


import os
import pprint


def walk_dir(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        pprint.pprint('[WARNING] {path} not exists'.format(path=path))
        return

    for d in os.listdir(path):
        pprint.pprint(d)


def run():
    walk_dir('/Users/lucas/projects/achilles/app/base')
    walk_dir('/rq')
    walk_dir('/sys')
    walk_dir('/var')


if __name__ == '__main__':
    run()
