#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : module_import_magic.py
# @Author: lucas
# @Date  : 9/3/18
# @Desc  :

import sys
import pprint


def mock():
    args = sys.argv
    pprint.pprint(args)
    if len(args) == 1:
        pprint.pprint('args length equals 1')
    elif len(args) == 2:
        pprint.pprint('args length equals 2')
    else:
        pprint.pprint('args length too many args!')


def run():
    mock()


if __name__ == '__main__':
    run()
