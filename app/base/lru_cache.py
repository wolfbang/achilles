#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lru_cache.py
# @Author: lucas
# @Date  : 9/22/18
# @Desc  :


from pprint import pprint


class LRUCache(object):
    """
    build-in LRU Cache
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]

        return -1

        pass

    def set(self, key, value):
        if len(self.cache) > self.capacity:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)

        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1


def run():
    lru = LRUCache(10)
    for x in range(0, 20):
        lru.set(x, x)

    for key, value in lru.cache.items():
        pprint('%s,%s' % (key, value))

    pprint(lru)


if __name__ == '__main__':
    run()
