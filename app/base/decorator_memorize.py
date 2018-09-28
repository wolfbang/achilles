#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator_memorize.py
# @Author: lucas
# @Date  : 9/28/18
# @Desc  :

from functools import wraps
from pprint import pprint
from collections import deque


class Memorized(object):
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.call_args_queue = deque()
        self.call_args_to_result = {}

    def __call__(self, fn, *args, **kwargs):
        @wraps(fn)
        def new_func(*args, **kwargs):  # fn args,kwargs
            memorization_key = self._convert_call_arguments_to_hash(args, kwargs)
            if memorization_key not in self.call_args_to_result:
                result = fn(*args, **kwargs)
                self._update_cache_key_with_value(memorization_key, result)
                self._evict_cache_if_necessary()

            return self.call_args_to_result[memorization_key]

        return new_func

    def _update_cache_key_with_value(self, key, value):
        self.call_args_to_result[key] = value
        self.call_args_queue.append(key)

    def _evict_cache_if_necessary(self):
        if len(self.call_args_queue) > self.cache_size:
            oldest_key = self.call_args_queue.popleft()
            del self.call_args_to_result[oldest_key]

    @staticmethod
    def _convert_call_arguments_to_hash(*args, **kwargs):
        return hash(str(args) + str(kwargs))


@Memorized(10)
def base():
    pprint('do base now!')
    return '[Base] Result'


def run():
    for i in range(0, 100):
        pprint(base())


if __name__ == '__main__':
    run()
