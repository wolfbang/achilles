#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : kwargs_traverse_magic.py
# @Author: lucas
# @Date  : 12/13/18
# @Desc  :


from pprint import pprint
from random import randint


class UserUpdate(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def update(user_id, user_update_form):
    return _update(user_id, **user_update_form.__dict__)


def _update(user_id, **kwargs):
    if not user_id:
        return
    pprint('user_id:{user_id},form:{form}'.format(user_id=user_id, form=kwargs))


def run():
    user_update = UserUpdate('simpson', '89561223')
    user_id = randint(10000, 20000)
    update(user_id, user_update)


if __name__ == '__main__':
    run()
