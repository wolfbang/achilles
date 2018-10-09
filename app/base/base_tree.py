#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base_tree.py
# @Author: lucas
# @Date  : 10/9/18
# @Desc  :


from pprint import pprint


class Tree(object):
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def total(root):
    if root is None:
        return 0
    return total(root.left) + total(root.right) + root.cargo


def print_tree(root):
    if not root:
        return

    pprint(root.cargo)
    print_tree(root.left)
    print_tree(root.right)


def print_tree_indented(root, level=0):
    if not root:
        return

    print_tree_indented(root.right, level + 1)

    pprint('  ' * level + str(root.cargo))
    print_tree_indented(root.left, level + 1)


def run():
    left_left = Tree(6)
    right_left = Tree(-3)

    left = Tree(1, left_left, right_left)

    left_right = Tree(10)
    right_right = Tree(90)
    right = Tree(3, left_right, right_right)

    root = Tree(5, left, right)
    pprint(total(root))

    pprint('====print tree')
    print_tree(root)

    pprint('====print tree indented')
    print_tree_indented(root)


if __name__ == '__main__':
    run()
