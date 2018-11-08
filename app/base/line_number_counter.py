#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : line_number_counter.py
# @Author: lucas
# @Date  : 9/30/18
# @Desc  :

import os
import functools
from pprint import pprint


def print_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if is_file_match(args[0]):
            pprint('%s' % args[0])
        result = func(*args, **kwargs)
        return result

    return wrapper


def is_file_match(path, file_type_list=('.java', '.py')):
    if not path:
        return False

    if not file_type_list:
        return False

    for f_type in file_type_list:
        if str(path).endswith(f_type):
            return True
    return False


@print_args
def get_line_number(path):
    line_number = 0
    if not os.path.isfile(path):
        return line_number

    if not is_file_match(path):
        return line_number

    with open(path, 'rb') as f:
        for x in f.readlines():
            line_number += 1
    return line_number


def read_file(path=None):
    is_exist = os.path.exists(path)
    line_number = 0
    if not is_exist:
        return line_number

    if os.path.isfile(path):
        line_number = get_line_number(path)

    elif os.path.isdir(path):
        files = os.listdir(path)

        for f in files:
            child_path = path + '/' + f
            if os.path.isfile(child_path):
                line_number += get_line_number(child_path)
            elif os.path.isdir(child_path):
                line_number += read_file(child_path)

    return line_number


def run():
    paths = ["/Users/lucas/projects/spacex-flask", "/Users/lucas/projects/spacex-rider",
             "/Users/lucas/projects/algo-dojo", "/Users/lucas/projects/spacex-shane", "/Users/lucas/projects/treasure",
             "/Users/lucas/projects/achilles", "/Users/lucas/projects/flask-rocket",
             "/Users/lucas/projects/sancho-panza","/Users/lucas/projects/pilot-hitchhiking"]

    total = 0
    for path in paths:
        line_number = read_file(path=path)

        if line_number > 0:
            total += line_number

    pprint('Total:%s' % total)


if __name__ == '__main__':
    run()
