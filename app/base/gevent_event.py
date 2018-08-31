#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gevent_event.py
# @Author: lucas
# @Date  : 8/31/18
# @Desc  :

import pprint
import gevent
from gevent.event import Event

evt = Event()


def setter():
    """
    it is a setter machine
    :return: 
    """
    pprint.pprint("[Setter]I'm about to sleep now")
    gevent.sleep(1)
    pprint.pprint("ok,I am done!")
    evt.set()


def waiter():
    """
    waiter machine
    :return: 
    """
    pprint.pprint('[Waiter]I will wait for you !')
    evt.wait()
    pprint.pprint("It's about time!")


def mock():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)

    ])


def run():
    mock()


if __name__ == '__main__':
    run()
