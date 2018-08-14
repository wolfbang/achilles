#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ternarys.py
# @Author: lucas
# @Date  : 8/14/18
# @Desc  :


def _get_boolean_results(condition):
    if not condition:
        return False
    result = "True" if condition else "False"
    print result, ',', type(result)


def _ternary_expression(condition):
    return True if condition else False


def _get_by_func(condition):
    result = _ternary_expression(condition)
    return result


def run():
    _get_boolean_results(True)
    _ternary_expression(True)
    _get_by_func(True)


if __name__ == '__main__':
    run()
