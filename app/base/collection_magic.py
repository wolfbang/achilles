#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : collection_magic.py
# @Author: lucas
# @Date  : 9/13/18
# @Desc  :


from pprint import pprint


class SuperEvent(dict):
    def __getitem__(self, key):
        value = super(SuperEvent, self).__getitem__(key)
        return '[{class_name}]:{value}'.format(class_name=self.__class__.__name__, value=value)


class Event(dict):
    def __getitem__(self, key):
        value = super(Event, self).__getitem__(key)
        return '[{class_name}]:{value}'.format(class_name=self.__class__.__name__, value=value)


def log_event_type():
    pprint('')


def run():
    event = Event(user='user', event_type='login', date='2018-09-13')
    pprint(event['user'])
    for key, value in event.items():
        pprint('%s,%s' % (key, value))

    import platform
    import sys
    pprint(sys.version)
    pprint(platform.version())


if __name__ == '__main__':
    run()
