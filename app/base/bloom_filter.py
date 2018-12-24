#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bloom_filter.py
# @Author: lucas
# @Date  : 12/18/18
# @Desc  :


import mmh3
from bitarray import bitarray
from pprint import pprint

BIT_SIZE = 5000000


class BloomFilter(object):
    def __init__(self):
        bit_array = bitarray(BIT_SIZE)
        bit_array.setall(0)
        self.bit_array = bit_array

    def add(self, url):
        point_list = self.get_positions(url)
        for b in point_list:
            self.bit_array[b] = 1

    def contains(self, url):
        point_list = self.get_positions(url)

        result = True
        for b in point_list:
            result = result and self.bit_array[b]
        return result

    @staticmethod
    def get_positions(url):
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE

        return [point1, point2, point3, point4, point5, point6, point7]


def bloom_filter_mock():
    bloom_filter_instance = BloomFilter()

    url1 = 'www.test1.com'
    url2 = 'www.test2.com'
    url3 = 'www.test3.com'
    url4 = 'www.test4.com'
    url5 = 'www.test5.com'
    bloom_filter_instance.add(url1)
    bloom_filter_instance.add(url2)
    bloom_filter_instance.add(url3)
    bloom_filter_instance.add(url4)
    bloom_filter_instance.add(url5)

    result = bloom_filter_instance.contains('www.example.com')
    pprint(result)

    result = bloom_filter_instance.contains(url1)
    pprint(result)

    pprint(bloom_filter_instance.bit_array)


def murmur_hash():
    hash_result = mmh3.hash('google')
    pprint(hash_result)

    hash64_result = mmh3.hash64('amazon')
    pprint(hash64_result)

    hash128_result = mmh3.hash128('HugeHard')
    pprint(hash128_result)


def run():
    murmur_hash()
    bloom_filter_mock()


if __name__ == '__main__':
    run()
