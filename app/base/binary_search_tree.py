#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: lucas
# @Date  : 9/29/18
# @Desc  :


from pprint import pprint


class TreeNode(object):
    """
    tree node definition,many operations are basic on this node
    """

    def __init__(self):
        self.left_node = None
        self.right_node = None

    def set_data(self, data):
        self.data = data

    def set_left_node(self, left_node):
        self.left_node = left_node

    def set_right_node(self, right_node):
        self.right_node = right_node

    def get_data(self):
        return self.data

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node


class BuildTree(object):
    """
    build binary search tree, leftNode is less than the rightNode
    """

    def build(self, data_list):
        """
        build binary search tree
        :param data_list: 
        :return: 
        """
        for i in range(len(data_list)):
            curr_data = data_list[i]
            new_tree_node = TreeNode()
            new_tree_node.set_data(curr_data)
            if i == 0:
                self.tree = new_tree_node
            else:
                flag_node = self.tree
                while flag_node is not None:
                    if curr_data <= flag_node.get_data():
                        if flag_node.get_left_node() is None:
                            flag_node.set_left_node(new_tree_node)
                            break
                        else:
                            flag_node = flag_node.get_left_node()
                    else:
                        if flag_node.get_right_node() is None:
                            flag_node.set_right_node(new_tree_node)
                            break
                        else:
                            flag_node = flag_node.get_right_node()

    def trans(self, temp_node):
        """
        LRD,Inorder Traversal
        :param temp_node: 
        :return: 
        """

        if temp_node is not None:
            self.trans(temp_node.get_left_node())
            if temp_node.get_left_node() is not None:
                temp_node2 = temp_node.get_left_node()
                while temp_node2.get_right_node() is not None:
                    temp_node2 = temp_node2.get_right_node()
                temp_node.set_left_node(temp_node2)
                temp_node2.set_right_node(temp_node)

            self.trans(temp_node.get_right_node())
            if temp_node.get_right_node() is not None:
                temp_node2 = temp_node.get_right_node()
                while temp_node2.get_left_node() is not None:
                    temp_node2 = temp_node2.get_left_node()

                temp_node.set_right_node(temp_node2)
                temp_node2.set_left_node(temp_node)

    def call_trans(self):
        """
        traverse tree
        :return: 
        """
        self.trans(self.tree)

    def print_it(self):

        """
        print tree
        :return: 
        """

        temp_node = self.tree
        while temp_node.get_left_node() is not None:
            temp_node = temp_node.get_left_node()

        # read left
        pprint('From Left to Right')
        while temp_node.get_right_node() is not None:
            pprint(temp_node.get_data())
            temp_node = temp_node.get_right_node()

        pprint(temp_node.get_data())

        # read right
        pprint('From Right To Left')
        while temp_node is not None:
            pprint(temp_node.get_data())
            temp_node = temp_node.get_left_node()


def run():
    data_list = [50, 1, 2, 3, 4, 5, 6, 7, 34, 8, 8, 90, 100]
    binary_search_tree = BuildTree()
    binary_search_tree.build(data_list)
    binary_search_tree.call_trans()
    binary_search_tree.print_it()


if __name__ == '__main__':
    run()
