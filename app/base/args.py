#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : args.py
# @Author: lucas
# @Date  : 8/5/18
# @Desc  :


def greetings(name='', content=''):
    print ' %s says: %s' % (name, content)


def run():
    greetings(content='never say never', name='Steve')


if __name__ == '__main__':
    run()
