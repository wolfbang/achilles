#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socket_server.py
# @Author: lucas
# @Date  : 9/24/18
# @Desc  :

import socket
from pprint import pprint


def init():
    s = socket.socket()
    host = socket.gethostname()
    pprint(host)

    port = 1234
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        pprint("Got Connect From:{}".format(addr))
        c.send("Thank you for connecting!")
        c.close()

    pass


def run():
    init()


if __name__ == '__main__':
    run()
