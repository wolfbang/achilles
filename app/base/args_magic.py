#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : args_magic.py
# @Author: lucas
# @Date  : 8/5/18
# @Desc  :


import pprint


def greetings(name='', content=''):
    print ' %s says: %s' % (name, content)


def test_var_args(f_arg, *args):
    pprint.pprint('the first args:%s' % f_arg)
    for arg in args:
        print 'another arg through *arg', arg


def test_args():
    test_var_args('facebook', 'google', 'python')
    test_var_args('tesla')


def run():
    greetings(content='never say never', name='Steve')
    test_args()


if __name__ == '__main__':
    run()
