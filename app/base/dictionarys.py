#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dictionarys.py
# @Author: lucas
# @Date  : 8/7/18
# @Desc  :


def _dict():
    dictionary = {}
    dictionary['a'] = 'alpha'
    dictionary['o'] = 'omega'
    dictionary['g'] = 'gamma'

    print dictionary

    print dictionary.get('a')
    print dictionary.get('notExist')

    print is_key_exist('a', dictionary=dictionary)
    print is_key_exist('b', dictionary=dictionary)
    print is_key_exist('z', dictionary=dictionary)
    _print_keys(dictionary=dictionary)
    _print_items(dictionary=dictionary)


def is_key_exist(key, dictionary):
    if dictionary is not None:
        if key in dictionary:
            return True
    return False


def _print_keys(dictionary):
    if not dictionary:
        return

    for key in dict(dictionary).keys():
        print key


def _print_items(dictionary):
    if not dictionary:
        return

    print '[print item]'
    for k, v in dict(dictionary).items():
        print k, v


def run():
    _dict()


if __name__ == '__main__':
    run()
