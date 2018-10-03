#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_traverse.py
# @Author: lucas
# @Date  : 10/3/18
# @Desc  :

import os
import re


def get_all_files(directory, extensions):
    extensions = [extension.lower() for extension in extensions]
    files = []

    for base, dirs, walk_files in os.walk(directory):
        for f in walk_files:
            if os.path.splitext(f)[1].lower() in extensions:
                files.append(os.path.join(base, f))
    return files


def natural_sort(raw_list):
    convert = lambda text: int(text) if text.isdigit() else text
    alpha_num_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    raw_list.sort(alpha_num_key)
    return raw_list


def run():
    from pprint import pprint
    pprint(get_all_files('/Users/lucas/projects/achilles', ['.py']))
    pprint(natural_sort(['1', '8', '12', '-12', '89', '3']))


if __name__ == '__main__':
    run()
