#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_search_tree.py
# @Author: lucas
# @Date  : 10/12/18
# @Desc  :


from pprint import pprint


class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_left_child(self):
        return self.parent and self.parent.left == self.left

    def is_right_child(self):
        return self.parent and self.parent.right == self.right

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def has_any_child(self):
        return self.left or self.right

    def has_both_children(self):
        return self.left and self.right

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left = lc
        self.right = rc

        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left)
            else:
                current_node.left = TreeNode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right)
            else:
                current_node.right = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None

        elif current_node.key == key:
            return current_node

        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            raise KeyError('no key:{0} in the tree!'.format(key))

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else:
            raise KeyError('no key:{0} in the tree!'.format(key))

    def __delitem__(self, key):
        self.delete(key)

    def traver_preorder(self, root):
        if not root:
            return

        current_node = root
        pprint('{},{}'.format(current_node.key, current_node.payload))
        self.traver_preorder(current_node.left)
        self.traver_preorder(current_node.right)

    def splice_out(self):
        pass

    def find_successor(self):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def remove(self, current_node):
        if not current_node:
            return

        if current_node.is_leaf():
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload

        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right_child():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:
                    current_node.replace_node_data(current_node.left.key,
                                                   current_node.left.payload,
                                                   current_node.left.left,
                                                   current_node.left.right)
            else:
                if current_node.is_left_child():
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)


def run():
    bst_tree = BinarySearchTree()
    bst_tree[1] = "google"
    bst_tree[4] = "amazon"
    bst_tree[6] = "facebook"
    bst_tree[2] = "air-bnb"

    pprint(bst_tree[6])
    pprint(bst_tree[2])
    pprint(bst_tree.size)
    pprint(bst_tree.put(10, 'linkedIn'))

    root = bst_tree.root
    bst_tree.traver_preorder(root)


if __name__ == '__main__':
    run()
