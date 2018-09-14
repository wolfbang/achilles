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

    def add(self, value):
        self.elements.append(value)

    def remove(self, value):
        self.elements.remove(value)

    def reverse(self):
        return self.elements.reverse()

    def get(self, index):
        if index is None:
            raise ValueError('index must not be null!')

        if not isinstance(index, int):
            raise ValueError('index must be integer!')

        if index < 0 or index > len(self.elements) - 1:
            raise ValueError('index out of bound!')

        return self.elements[index]


def run():
    s1 = ListBaseSet('windows')
    s2 = ListBaseSet('navigator')
    pprint(s1)
    pprint(s2)
    s1.add(['X', 'Y', 'Z'])
    pprint(s1)
    s1.remove('w')
    pprint(s1)
    s1.get(1)
    pprint(s1.get(3))


if __name__ == '__main__':
    run()
