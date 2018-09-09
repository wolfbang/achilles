#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dir_func.py
# @Author: lucas
# @Date  : 9/9/18
# @Desc  :


class Device(object):
    def __init__(self, device_id, os_type):
        self.device_id = device_id
        self.os_type = os_type

    def __str__(self):
        return str(self.__dict__)


def run():
    device = Device('SDOAODSJAPKUU&JHKHHHB', 'iOS')
    print device
    dir_info = dir(device)
    print dir_info
    print hasattr(device, 'name')
    print getattr(device, '__str__')
    print getattr(device, '__dict__')

    from datetime import datetime
    device.created_time = datetime.now()
    print device


if __name__ == '__main__':
    run()
