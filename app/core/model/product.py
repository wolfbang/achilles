#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : product.py
# @Author: lucas
# @Date  : 9/6/18
# @Desc  :


class Product(object):
    total = 0

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        Product.total += 1

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def more_than_one():
        return Product.total > 1

    @classmethod
    def get_info(cls):
        info = 'info:{} '.format(cls.total)
        print info


def run():
    import random
    pid = random.randint(1000, 9000)
    p = Product(pid, 'iPhone', 12)
    bid = random.randint(1000, 9000)
    beer = Product(bid, 'Beer', 5)
    print p, beer
    print Product.total
    print Product.more_than_one()


if __name__ == '__main__':
    run()
