#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forloop_magic.py
# @Author: lucas
# @Date  : 8/14/18
# @Desc  :


def _not_found(target):
    print '[Not Found] target:%s' % target


def _for_else(container, target):
    if not container:
        return

    for element in container:
        if element == target:
            print '[Found]', element
            break

    else:
        _not_found(target)


def run():
    target = 20
    boundary = 20
    list_container = [x for x in range(0, boundary)]
    _for_else(list_container, target)


if __name__ == '__main__':
    run()
