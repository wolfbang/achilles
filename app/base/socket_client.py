#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socket_client.py
# @Author: lucas
# @Date  : 9/24/18
# @Desc  :

import socket
from pprint import pprint


def connect():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    pprint(s.recv(1024))
    pass


def run():
    connect()


if __name__ == '__main__':
    run()
