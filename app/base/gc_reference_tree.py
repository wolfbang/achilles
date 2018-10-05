#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gc_reference_tree.py
# @Author: lucas
# @Date  : 10/4/18
# @Desc  :


import gc
from pprint import pprint


class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next_node):
        pprint('Linking nodes %s.next = %s' % (self, next_node))
        self.next = next_node

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)


def build_gc_tree():
    root = Graph('root')
    node_x = Graph('node-x')
    node_y = Graph('node-y')
    node_z = Graph('node-z')
    root.set_next(node_x)
    node_x.set_next(node_y)
    node_y.set_next(node_z)

    for tree_node in gc.get_referents(node_z):
        pprint(type(tree_node))
        pprint(tree_node)


def run():
    build_gc_tree()


if __name__ == '__main__':
    run()
