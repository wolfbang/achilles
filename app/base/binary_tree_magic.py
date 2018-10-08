#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_tree_magic.py
# @Author: lucas
# @Date  : 10/8/18
# @Desc  :


from pprint import pprint


class SimpleTree(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def traverse_preorder(self, root):
        if not root:
            return

        pprint(root.data)
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)

    def traverse_inorder(self, root):
        if not root:
            return

        self.traverse_inorder(root.left)
        pprint(root.data)
        self.traverse_inorder(root.right)

    def traverse_postorder(self, root):
        if not root:
            return

        self.traverse_postorder(root.right)
        self.traverse_postorder(root.left)
        pprint(root.data)


def run():
    root = SimpleTree('root', None, None)

    child_left = SimpleTree('left', None, None)
    child_right = SimpleTree('right', None, None)

    root.left = child_left
    root.right = child_right

    grand_child_left = SimpleTree('grand-child-left', None, None)
    grand_child_right = SimpleTree('grand-child-right', None, None)

    child_left.left = grand_child_left
    child_right.right = grand_child_right

    root.traverse_preorder(root)

    pprint('### in order ###')
    root.traverse_inorder(root)

    pprint('### post order ###')
    root.traverse_postorder(root)


if __name__ == '__main__':
    run()
