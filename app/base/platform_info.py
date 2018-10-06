#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : platform_info.py
# @Author: lucas
# @Date  : 10/6/18
# @Desc  :


import platform
from pprint import pprint


def platform_info():
    platform.platform()
    version = platform.version()
    arch = platform.architecture()
    machine = platform.machine()
    node = platform.node()
    uname = platform.uname()
    system = platform.system()
    processor = platform.processor()
    py_branch = platform.python_branch()
    py_version = platform.python_version()

    system_info_list = ['version', 'arch', 'machine', 'node', 'uname', 'system', 'processor', 'py_branch', py_version]
    system_value_list = [version, arch, machine, node, uname, system, processor, py_branch, py_version]

    pprint(zip(system_info_list, system_value_list))


def run():
    platform_info()


if __name__ == '__main__':
    run()
