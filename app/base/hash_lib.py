#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hash_lib.py
# @Author: lucas
# @Date  : 9/25/18
# @Desc  :

import hashlib
from pprint import pprint


def md5_hashing():
    raw_content = 'Julius Caesar'
    md5 = hashlib.md5()
    md5.update(raw_content)
    pprint(md5.hexdigest())


def sha_hashing():
    """
    [WARNING]
    sha1 is a little bit slow
    :return: 
    """
    raw_content = 'Julius Caesar'
    sha1 = hashlib.sha1()
    sha1.update(raw_content)
    pprint(sha1.hexdigest())

    sha256 = hashlib.sha256()
    sha256.update(raw_content)
    pprint(sha256.hexdigest())

    sha384 = hashlib.sha384()
    sha384.update(raw_content)
    pprint(sha384.hexdigest())

    sha512 = hashlib.sha512()
    sha512.update(raw_content)
    pprint(sha512.hexdigest())


def run():
    md5_hashing()
    sha_hashing()


if __name__ == '__main__':
    run()
