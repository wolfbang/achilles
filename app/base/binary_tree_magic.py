#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_tree_magic.py
# @Author: lucas
# @Date  : 10/8/18
# @Desc  :


from pprint import pprint


class Node(object):
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __str__(self):
        return 'Node({})'.format(self.data)


class SimpleTree(object):
    """
    a simple binary tree
    """
    def insert(self, node, data):
        """
        insert a node
        :param node: 
        :param data: 
        :return: 
        """

        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)

        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        """
        binary search
        :param node: 
        :param data: 
        :return: 
        """
        if node is None or node.data == data:
            return node
        elif node.data < data:
            return self.search(node.right, data)
        elif node.data > data:
            return self.search(node.left, data)

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
    root = Node(10)

    tree = SimpleTree()
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 10)
    tree.insert(root, -13)
    tree.insert(root, 100)

    pprint(tree)

    pprint('### pre order ###')
    tree.traverse_preorder(root)

    pprint('### in order ###')
    tree.traverse_inorder(root)

    pprint('### post order ###')
    tree.traverse_postorder(root)

    pprint(tree.search(root, 10))


if __name__ == '__main__':
    run()
