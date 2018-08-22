#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dictonary_content.py
# @Author: lucas
# @Date  : 8/21/18
# @Desc  :


import pprint


def __print_dictionary_content(file_path):
    import os
    for sChild in os.listdir(file_path):
        s_child_path = os.path.join(file_path, sChild)

        if os.path.isdir(s_child_path):
            __print_dictionary_content(s_child_path)
        else:
            pprint.pprint(s_child_path)


def run():
    __print_dictionary_content('/Users/lucas/projects/achilles')


if __name__ == '__main__':
    run()
