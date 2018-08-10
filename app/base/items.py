#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : items.py
# @Author: lucas
# @Date  : 8/9/18
# @Desc  :

from random import randint


def get_first(items):
    return list(items)[0] if items else None


def run():
    users = []
    for i in range(0, 10):
        users.append(randint(1, 100))

    print '[Generator]', users
    users_after_selected = [uid for uid in users if uid >= 20]

    for uid in users_after_selected:
        print uid

    print '[GetFirst]', get_first(users_after_selected)
    print '[GetFirst]', get_first(None)


if __name__ == '__main__':
    run()
