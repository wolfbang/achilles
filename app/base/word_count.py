#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : word_count.py
# @Author: lucas
# @Date  : 8/6/18
# @Desc  :

import sys


def word_count_dict(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if not word in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] = word_count[word] + 1

    return word_count


def get_word_count(filename):
    word_count = word_count_dict(filename)
    print word_count


def print_words(filename):
    word_count = word_count_dict(filename)
    words = sorted(word_count.keys())
    for word in words:
        print word, word_count[word]


def get_count(word_count_tuple):
    return word_count_tuple[1]


def print_top(filename):
    word_count = word_count_dict(filename)
    items = sorted(word_count.items(), key=get_count, reverse=True)
    print '[print top]'
    for item in items[:20]:
        print item[0], item[1]


def run():
    filename = '/Users/lucas/projects/achilles/app/base/args_magic.py'
    get_word_count(filename)
    print_words(filename)
    print_top(filename)


if __name__ == '__main__':
    run()
