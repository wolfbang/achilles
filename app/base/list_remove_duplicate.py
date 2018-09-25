#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : list_remove_duplicate.py
# @Author: lucas
# @Date  : 9/25/18
# @Desc  :


from pprint import pprint


def remove_duplicate(raw_list):
    if not raw_list:
        return

    target_list = []
    for item in raw_list:
        if item not in target_list:
            target_list.append(item)
    return target_list


def smart_remove_duplicate(raw_list):
    if not raw_list:
        return
    return list(set(raw_list))


def run():
    numbers = [1, 2, 4, 5, 5, 5, 5, 90]
    pprint(remove_duplicate(numbers))
    pprint(smart_remove_duplicate(numbers))
    pprint(smart_remove_duplicate(None))


if __name__ == '__main__':
    run()
