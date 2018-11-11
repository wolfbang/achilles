#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : lambda_basic.py
# @Author: lucas
# @Date  : 11/10/18
# @Desc  :


from pprint import pprint


def normalize(string):
    return str(string).upper()


def run():
    colors = ['Green', "Goldenrod", 'Cyan', "Purple", "Turquoise"]
    normalize_colors = map(normalize, colors)
    pprint(normalize_colors)

    lambda_color = map(lambda x: x.upper(), colors)
    pprint(lambda_color)


if __name__ == '__main__':
    run()
