#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : proxy_mapping.py
# @Author: lucas
# @Date  : 9/26/18
# @Desc  :


import functools
import random
import sys
from pprint import pprint

USER_PROXY_SWITCH_KEY = 'user:proxy:switch'


class Switch(object):
    @staticmethod
    def is_switched_on(USER_PROXY_SWITCH_KEY):
        return True


class FakeUser(object):
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def new_get(uid):
    user = FakeUser(uid, 'proxy-user-%s' % (random.randint(0, sys.maxint)))
    return user


def user_hitter(uid, *args):
    if not uid:
        return False
    return uid % 2 == 0 and uid > 50


def proxy_get(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) <= 0:
            pprint('[Warning] no parameters! method:%s' % func.func_name)
            return func(*args, **kwargs)
        args1 = args[0]
        if Switch.is_switched_on(args1):
            if not user_hitter(args1):
                return func(*args, **kwargs)
            # proxy get by new func
            method_name = func.func_name
            proxy_target_method = global_method_mapping().get(method_name, None)
            if proxy_target_method:
                return proxy_target_method(*args, **kwargs)
            else:
                return

                # get by old func
        return func(*args, **kwargs)

    return wrapper


@proxy_get
def get(uid):
    user = FakeUser(uid, 'no-proxy-%s' % (random.randint(0, sys.maxint)))
    # pprint('no proxy:%s' % user)
    return user


@proxy_get
def query():
    pprint('query invoked!')


def global_method_mapping():
    method_map = {'get': new_get}
    return method_map


def run():
    for uid in range(100):
        user = get(uid)
        pprint(user)

    query()


if __name__ == '__main__':
    run()
