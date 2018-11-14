#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_line_counter.py
# @Author: lucas
# @Date  : 11/14/18
# @Desc  :

from pprint import pprint
import os


def count_line(file_path):
    if not os.path.exists(file_path):
        return 0

    line_number = 0
    with open(file_path, 'rb') as f:
        for line in f.readlines():
            line_number = line_number + 1

    return line_number


def run():
    total = count_line('/Users/lucas/projects/achilles/app/base/file_line_counter.py')
    pprint(total)


if __name__ == '__main__':
    run()
