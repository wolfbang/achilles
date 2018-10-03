#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : folder_clean.py
# @Author: lucas
# @Date  : 10/4/18
# @Desc  :


import os
import shutil


def move_and_clean():
    cur_dir = os.getcwd()
    docx = [x for x in os.listdir(cur_dir) if os.path.splitext(x)[1] in ('.docx', '.doc')]
    docx_dir = cur_dir + os.sep + 'docs'

    if len(docx) > 0:
        try:
            os.mkdir(docx_dir)
        except Exception as e:
            if not os.path.isdir(docx_dir):
                raise
        for i in docx:
            shutil.move(cur_dir + os.sep + i, docx_dir)
    pass


def run():
    move_and_clean()


if __name__ == '__main__':
    run()
