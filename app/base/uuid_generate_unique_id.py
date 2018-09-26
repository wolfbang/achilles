#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : uuid_generate_unique_id.py
# @Author: lucas
# @Date  : 9/26/18
# @Desc  :


import uuid
import hashlib
import random
import string
from pprint import pprint


def md5(s):
    return hashlib.new('md5', s).hexdigest()


def sha1(s):
    return hashlib.new('sha1', s).hexdigest()


def random_number(length):
    return random.randrange(10 ** (length - 1), 10 ** length)


def get_random_string(length):
    assert length > 0
    return ''.join(random.choice(string.digits + string.letters) for x in range(length))


def get_unique_string(length=31, hash_func=md5):
    uid = uuid.uuid1()
    pprint(type(uid))
    full = hash_func(uid.hex)

    if length > 0:
        return full[:length]
    else:
        return full


def run():
    unique_string = get_unique_string()
    pprint(unique_string)

    unique_string = get_unique_string(hash_func=sha1)
    pprint(unique_string)

    random_num = random_number(10)
    pprint(random_num)

    random_string = get_random_string(10)
    pprint(random_string)


if __name__ == '__main__':
    run()
