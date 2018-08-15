#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : file_reader.py
# @Author: lucas
# @Date  : 8/15/18
# @Desc  :


def _read_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        return data


def _is_jpg_file(file_data):
    if not file_data:
        return False

    if file_data.startswith(b'\xff\xd8'):
        return True
    else:
        return False


def run():
    file_path = '/Users/lucas/projects/achilles/app/base/file_reader.py'
    file_path = '/Users/lucas/Downloads/appStore.jpg'
    data = _read_file(filepath=file_path)
    is_jpg = _is_jpg_file(file_data=data)

    message = "{0} is JPG file!".format(file_path) if is_jpg else "{0} is not JPG file!".format(file_path)
    print message


if __name__ == '__main__':
    run()
