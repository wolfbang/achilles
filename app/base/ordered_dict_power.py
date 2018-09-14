#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ordered_dict_power.py
# @Author: lucas
# @Date  : 9/13/18
# @Desc  :


from pprint import pprint
from collections import OrderedDict


class LastUpdateOrderDict(OrderedDict):
    def __setitem__(self, key, value):
        if key in self.keys():
            del self[key]
        super(LastUpdateOrderDict, self).__setitem__(key, value)

    pass


def build_dict():
    return {'banana': 3, 'pear': 4, 'apple': 5, 'grape': 1}


def order_dict():
    d = build_dict()
    for x in d.items():
        pprint(type(x))
    order_dictionary = OrderedDict(sorted(d.items(), key=lambda item: item[0]))
    pprint(order_dictionary)

    order_dictionary = OrderedDict(sorted(d.items(), key=lambda item: item[1]))
    pprint(order_dictionary)

    order_dictionary = OrderedDict(sorted(d.items(), key=lambda item: len(item[0])))
    pprint(order_dictionary)


def last_update_order_dict():
    d = build_dict()
    order_d = OrderedDict(sorted(d.items(), key=lambda item: item[0]))
    order_dictionary = LastUpdateOrderDict(sorted(order_d.items(), key=lambda item: item[0]))
    pprint('order_dictionary:{}'.format(order_dictionary))
    order_dictionary['orange'] = 2
    pprint(LastUpdateOrderDict(sorted(order_dictionary.items(), key=lambda item: item[0])))


def run():
    order_dict()
    last_update_order_dict()


if __name__ == '__main__':
    run()
