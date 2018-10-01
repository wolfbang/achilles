#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : context_management.py
# @Author: lucas
# @Date  : 10/1/18
# @Desc  :


from contextlib import contextmanager


@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()


def run():
    path = 'test.log'
    with make_open_context(path, 'wb+') as f:
        f.write('message from context management!')


if __name__ == '__main__':
    run()
