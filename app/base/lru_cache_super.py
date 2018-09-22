#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lru_cache_super.py
# @Author: lucas
# @Date  : 9/22/18
# @Desc  :

from pprint import pprint
from collections import OrderedDict


class LRUCache(OrderedDict):
    """
    LRU Cache
    """

    def __init__(self, capacity, *args, **kwds):
        super(LRUCache, self).__init__(*args, **kwds)
        self.capacity = capacity
        self.cache = OrderedDict()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)

        self.cache[key] = value


def run():
    lru = LRUCache(10)
    for x in range(0, 15):
        lru.set(x, x)
    pprint(lru.cache)
    pprint(lru.get(10))


if __name__ == '__main__':
    run()
