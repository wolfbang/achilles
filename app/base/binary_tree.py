#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_tree.py
# @Author: lucas
# @Date  : 9/29/18
# @Desc  :


from pprint import pprint


class TreeNode(object):
    """
    binary tree
    """

    def __init__(self):
        self.left_node = None
        self.right_node = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left_node(self, left_node):
        self.left_node = left_node

    def get_left_node(self):
        return self.left_node

    def set_right_node(self, right_node):
        self.right_node = right_node

    def get_right_node(self):
        return self.right_node


class BuildTree(object):
    """
    build the tree
    """

    def __init__(self):
        self.index = 0
        self.data = [10, 5, 4, None, 3, None, None, 7, None, None, 12, None, None]
        self.tree = self.build_node()
        temp_node = self.tree
        data_list = []
        self.find_sum(temp_node, 22, data_list)

    def build_node(self):
        """
        build node recursively
        """

        if self.index < len(self.data):
            curr_data = self.data[self.index]
            self.index = self.index + 1
            if curr_data is not None:
                on_node = TreeNode()
                on_node.set_data(curr_data)
                left_node = self.build_node()
                on_node.set_left_node(left_node)
                right_node = self.build_node()

                on_node.set_right_node(right_node)
                return on_node

    def find_sum(self, node, need_sum, data_list):

        if node is not None and node.get_data() <= need_sum:
            if node.get_data() < need_sum:
                new_sum = need_sum - node.get_data()
                curr_data = node.get_data()
                data_list.append(curr_data)
                self.find_sum(node.get_left_node(), new_sum, data_list)
                self.find_sum(node.get_right_node(), new_sum, data_list)
                data_list.pop()
            else:
                if node.get_data() == need_sum:
                    for data in data_list:
                        pprint(data)

                    pprint(node.get_data())
                    print '-----------'


def run():
    tree = BuildTree()


if __name__ == '__main__':
    run()
