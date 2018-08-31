#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : deco_users.py
# @Author: lucas
# @Date  : 8/31/18
# @Desc  :

import pprint

USERS = {}


def new_user(username, password):
    global USERS
    USERS[username] = password


def authenticate(username, password):
    if USERS.get(username) == password:
        return True

    return False


def run():
    new_user('lucas', 'password')
    pprint.pprint(USERS)
    pprint.pprint(authenticate('lucas', 'random'))
    pprint.pprint(authenticate('lucas', 'password'))
    pprint.pprint(authenticate('java', 'password'))


if __name__ == '__main__':
    run()
