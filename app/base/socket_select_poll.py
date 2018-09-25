#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socket_select_poll.py
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
    fdmap = {s.fileno(): s}

    s.listen(5)
    p = select.poll()
    p.register(s)

    while True:
        events = p.poll()
        for fd, event in events:
            if fd == s.fileno():
                c, addr = s.accept()
                pprint('Got connection from:{}' % (addr))
                p.register(c)
                fdmap[c.fileno()] = c
            elif event & select.POLLIN:
                data = fdmap[fd].recv(1024)
                if not data:
                    pprint('{} disconnected!' % (fdmap[fd].getpeername()))
                    p.unregister(fd)
                    del fdmap[fd]

            else:
                pprint(data)


def run():
    init()


if __name__ == '__main__':
    run()
