#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tree_height.py
# @Author: lucas
# @Date  : 10/11/18
# @Desc  :


from pprint import pprint


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_height(root):
    if not root:
        return 0

    return 1 + max(get_height(root.left), get_height(root.right))


def traverse_preorder(root):
    if not root:
        return

    pprint(root.data)
    traverse_preorder(root.left)
    traverse_preorder(root.right)


def run():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    i = TreeNode(9)

    a.left, a.right = b, c

    b.left = d
    d.left, d.right = e, f
    f.left = g
    g.left, g.right = h, i

    height = get_height(a)
    pprint(height)

    pprint('print tree pre order ')
    traverse_preorder(root=a)


if __name__ == '__main__':
    run()
