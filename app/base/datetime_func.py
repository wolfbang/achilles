#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : datetime_func.py
# @Author: lucas
# @Date  : 9/25/18
# @Desc  :


import datetime
import time
from pprint import pprint


def base():
    now = datetime.datetime.now()
    pprint(type(now))
    pprint(now)
    tp = now.timetuple()
    timestamp = time.mktime(tp)
    pprint((timestamp, type(timestamp)))

    make_time = datetime.datetime.fromtimestamp(timestamp)
    pprint(type(make_time))
    pprint(make_time)


def format_datetime():
    now = datetime.datetime.now()
    formatter = '%Y-%m-%d %H:%M:%S'
    pprint(datetime.datetime.strftime(now, formatter))


def str2datetime():
    """
    Y => xxxx(year)
    m => xx(month)
    d => xx(day)
    
    H => xx(24-hour)
    M => xx(minute)
    S => xx(second)
    :return: 
    """
    date_str = '2018-09-27 23:58:58'
    format_pattern = '%Y-%m-%d %H:%M:%S'
    date_time = datetime.datetime.strptime(date_str, format_pattern)
    pprint(date_time)


def difference():
    start = time.time()
    time.sleep(1)
    end = time.time()
    pprint(end - start)


def run():
    base()
    difference()
    format_datetime()
    str2datetime()


if __name__ == '__main__':
    run()
