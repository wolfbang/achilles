#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : back_up_script.py
# @Author: lucas
# @Date  : 10/3/18
# @Desc  :

import os
import time
from pprint import pprint


def back_up():
    source = ['/Users/lucas/projects/achilles']
    target_dir = '/Users/lucas/projects/achilles/backup'

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    comment = raw_input('please enter a comment ----->')

    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + str(comment).replace(' ', '_') + '.zip'

    if not os.path.exists(today):
        os.mkdir(today)
        pprint('successfully create dir %s' % today)

    zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

    pprint('zip command is: %s' % zip_command)
    pprint('Running')

    if os.system(zip_command) == 0:
        pprint('successfully back up to: %s' % target)
    else:
        pprint('Backup FAILED!')


def run():
    back_up()


if __name__ == '__main__':
    run()
