#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : subprocess_client.py
# @Author: lucas
# @Date  : 9/16/18
# @Desc  :


import subprocess
from subprocess import Popen, PIPE
from pprint import pprint


def call_command(command):
    subprocess.call(command, shell=True)


def popen():
    p1 = Popen(['ps', '-ef'], stdout=PIPE)
    p2 = Popen(['grep', 'redis'], stdin=p1.stdout, stdout=PIPE)
    p3 = Popen(['grep', '-v', 'grep'], stdin=p2.stdout, stdout=PIPE)
    stdout, _ = p3.communicate()
    pprint('stdout={}'.format(stdout))
    pass


def run():
    command = 'ls -alF'
    call_command(command)
    call_command('ulimit -a')
    popen()


if __name__ == '__main__':
    run()
