#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : counter_magic.py
# @Author: lucas
# @Date  : 9/13/18
# @Desc  :


from pprint import pprint
from collections import Counter
import re


def super_word_counter(path='', most_common_number=10):
    """super word counter"""
    with open(path, 'rb') as text_file:
        text = text_file.read().lower()
    words = re.findall(r'\w+', text)

    most_common_words = Counter(words).most_common(most_common_number)
    pprint(most_common_words)
    return most_common_words


def simple_word_counter():
    """simple word counter"""
    counter = Counter()
    words = ['red', 'blue', 'red', 'green', 'red', 'pink']

    for word in words:
        counter[word] += 1

    pprint(counter)


def run():
    simple_word_counter()
    super_word_counter(path='/Users/lucas/Downloads/hamlet.txt', most_common_number=20)


if __name__ == '__main__':
    run()
