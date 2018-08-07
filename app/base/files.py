#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : files.py
# @Author: lucas
# @Date  : 8/7/18
# @Desc  :


import codecs


def _file_content_with_codec(filename):
    if not filename:
        return

    with codecs.open(filename, 'rU', 'utf-8') as f:
        for line in f:
            print line


def _file_content(filename):
    if not filename:
        return
    with open(filename) as f:
        for line in f:
            print line


def run():
    filename = '/Users/lucas/projects/achilles/.gitignore'
    py_file = '/Users/lucas/projects/achilles/app/app.py'
    _file_content(filename=filename)
    _file_content_with_codec(filename=py_file)


if __name__ == '__main__':
    run()
