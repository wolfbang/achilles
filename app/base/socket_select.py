#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socket_select.py
# @Author: lucas
# @Date  : 9/24/18
# @Desc  :

import socket
import select
from pprint import pprint


def init():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.bind((host, port))
    s.listen(5)
    inputs = [s]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is s:
                c, addr = s.accept()
                pprint('Got connected from:{address}'.format(address=addr))
                inputs.append(c)
            else:
                try:
                    data = r.recv(1024)
                    disconnected = not data
                except socket.error:
                    disconnected = True

                if disconnected:
                    pprint('{} disconnected'.format(r.getpeername()))
                    inputs.remove(r)
                else:
                    pprint(data)


def run():
    init()


if __name__ == '__main__':
    run()
