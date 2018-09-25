#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : encrypt_password.py
# @Author: lucas
# @Date  : 9/25/18
# @Desc  :

import os
from hashlib import sha256
from hmac import HMAC
from pprint import pprint


def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)

    assert len(salt) == 8
    assert isinstance(salt, str)
    if isinstance(password, unicode):
        password = password.encode('utf-8')

    assert isinstance(password, str)
    result = password
    for x in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


def run():
    password = 'my-test'
    hashed = encrypt_password(password)
    pprint(hashed)
    is_equal = validate_password(hashed, password)
    pprint(is_equal)


if __name__ == '__main__':
    run()
