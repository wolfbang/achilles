#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : os_type.py
# @Author: lucas
# @Date  : 9/16/18
# @Desc  :

import os
import errno
from pprint import pprint


def listdir(dirname):
    try:
        os.listdir(dirname)
    except OSError as e:
        error = e.errno
        if errno == errno.ENOENT:
            pprint('path:{} ,No such file or directory!'.format(dirname))
        elif error == errno.EACCES:
            pprint('path:{},Permission Denied'.format(dirname))
        elif error == errno.ENOSPC:
            pprint('path:{}, NO space on device'.format(dirname))
        else:
            pprint('path:{},{}'.format(dirname, e.strerror))
    else:
        pprint('path:{}, No Error! '.format(dirname))


def run():
    paths = ['/root', '/home', '/no/such/dir']
    for path in paths:
        listdir(path)


if __name__ == '__main__':
    run()
