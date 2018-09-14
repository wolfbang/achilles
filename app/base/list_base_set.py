#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_base_set.py
# @Author: lucas
# @Date  : 9/14/18
# @Desc  :


from collections import Set
from pprint import pprint


class ListBaseSet(Set):
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


def run():
    s1 = ListBaseSet('windows')
    s2 = ListBaseSet('navigator')
    pprint(s1)
    pprint(s2)


if __name__ == '__main__':
    run()
