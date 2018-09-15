#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : point_tuple.py
# @Author: lucas
# @Date  : 9/14/18
# @Desc  :


from collections import namedtuple
from pprint import pprint


class Point(namedtuple('Point', 'x y')):
    __slot__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) * 0.5

    def __str__(self):
        return str(self.__dict__)


def get_3d_point(x, y, z):
    Point3D = namedtuple('Point3D', Point._fields + ('z',))
    point_3d = Point3D(x, y, z)
    return point_3d


def run():
    for p in Point(1, 3), Point(2, 4):
        pprint(p)
        pprint(p.hypot)

    point_3d = get_3d_point(1, 6, 7)
    pprint(point_3d)


if __name__ == '__main__':
    run()
