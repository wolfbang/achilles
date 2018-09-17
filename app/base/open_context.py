#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : open_context.py
# @Author: lucas
# @Date  : 9/17/18
# @Desc  :

from pprint import pprint
from contextlib import contextmanager, nested


class OpenContext(object):
    def __init__(self, filename, mode):
        self.fp = open(filename, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()


@contextmanager
def make_context(*args):
    pprint(args)
    yield


def run():
    with OpenContext('open.log', 'a') as f:
        f.write('\n message from open context!')

    with make_open_context('open.log', 'a') as f:
        f.write('\n message from make_open_context!')

    with make_context(1, 2) as A:
        with make_context(3, 4) as B:
            pprint('In the context')

    with make_context(1, 2) as A, make_context(3, 4) as B:
        pprint('In the context!')

    with nested(make_context(1, 2)), make_context(3, 4) as B:
        pprint('[With Nested]In the context!')


if __name__ == '__main__':
    run()
