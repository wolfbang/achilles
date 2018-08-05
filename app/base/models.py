#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : models.py
# @Author: lucas
# @Date  : 8/4/18
# @Desc  :


class BusyLevel:
    def __init__(self):
        pass

    CLOSE = 0
    OPEN = 0


class Restaurant:
    """ Restaurant """

    id = 0
    oid = 0
    is_valid = 0
    agent_fee = 0
    busy_level = BusyLevel.CLOSE
    description = ''
    address = ''
    image_url = ''
    name = ''

    def __init__(self):
        pass
