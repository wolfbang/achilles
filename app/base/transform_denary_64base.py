#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : transform_denary_64base.py
# @Author: lucas
# @Date  : 9/26/18
# @Desc  :

from pprint import pprint
import sys


def encode_base64(number):
    """
    denary to 64
    result stored from low to high,need to reverse in the end
    :param number: 
    :return: 
    """
    table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    result = []
    temp = number

    if temp == 0:
        result.append('0')
    else:
        while 0 < temp:
            result.append(table[temp % len(table)])
            temp /= 64

    return ''.join([x for x in reversed(result)])


def decode_base64(num_string):
    """
    string to number
    :param num_string: 
    :return: 
    """

    table_mapping = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                     "6": 6, "7": 7, "8": 8, "9": 9,
                     "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16,
                     "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23,
                     "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
                     "v": 31, "w": 32, "x": 33, "y": 34, "z": 35,
                     "A": 36, "B": 37, "C": 38, "D": 39, "E": 40, "F": 41, "G": 42,
                     "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49,
                     "O": 50, "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56,
                     "V": 57, "W": 58, "X": 59, "Y": 60, "Z": 61,
                     "-": 62, "_": 63}

    result = 0
    for i in xrange(len(num_string)):
        result *= 64
        result += table_mapping[num_string[i]]

    return result


def run():
    str1 = encode_base64(1231290)
    pprint(str1)

    str2 = encode_base64(98786767565)
    pprint(str2)

    str3 = encode_base64(sys.maxint)
    pprint(str3)
    pprint(sys.maxint)

    num_one_hundred_million = 100000000
    str_one_hundred_million = encode_base64(num_one_hundred_million)
    pprint(str_one_hundred_million)
    pprint(decode_base64(str_one_hundred_million) == num_one_hundred_million)


if __name__ == '__main__':
    run()
