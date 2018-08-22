#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : context_manager.py
# @Author: lucas
# @Date  : 8/22/18
# @Desc  :


import pprint


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exception has been handled")
        self.file_obj.close()
        return True


def __custom_open_file(text='add some log'):
    with File('open.log', 'w') as f:
        f.write(text)
    pprint.pprint('{func_name} is executed!'.format(func_name='__custom_open_file'))


def open_file(file_path, text='some text'):
    if file_path:
        with open(file_path, 'w') as opened_file:
            opened_file.write(text)
            # opened_file.undefined_function()
    pprint.pprint('[Manager] done')


def run():
    open_file('log.log', text='say something please')
    __custom_open_file()


if __name__ == '__main__':
    run()
