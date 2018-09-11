#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : enum_type.py
# @Author: lucas
# @Date  : 9/10/18
# @Desc  :

from enum import Enum, unique

Month = Enum('Month', (
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
))


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Sat = 3
    Thur = 4
    Fri = 5
    Sat = 6
    Sun = 7


def iter_month():
    for name, member in Month.__members__.items():
        print name, '=>', member, ',', member.value


def mock_weekday():
    day_one = Weekday.Mon
    day_two = Weekday.Tue
    print day_one
    print day_two


def run():
    iter_month()
    mock_weekday()


if __name__ == '__main__':
    run()
