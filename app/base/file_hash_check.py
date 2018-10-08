#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_hash_check.py
# @Author: lucas
# @Date  : 10/7/18
# @Desc  :


import os
import hashlib
from pprint import pprint


def file_hash(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()
        return sha256


def compare(file_path_x, file_path_y):
    if file_hash(file_path_x) == file_hash(file_path_y):
        pprint('[Not Equal] {} ,{} check sum result!'.format(file_path_x, file_path_y))
        return True
    else:
        pprint('[Equal] {} ,{} check sum result!'.format(file_path_x, file_path_y))
        return False


def run():
    file_path_x = 'file_hash_check.py'
    file_path_y = 'file_traverse.py'

    compare(file_path_x, file_path_y)


if __name__ == '__main__':
    run()
