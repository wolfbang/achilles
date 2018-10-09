#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : trie_tree.py
# @Author: lucas
# @Date  : 10/9/18
# @Desc  :



from pprint import pprint


class TrieTree(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

    def add(self, root, word):
        node = root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break

            if not found_in_child:
                new_node = TrieTree(char)
                node.children.append(new_node)
                node = new_node

        node.word_finished = True

    def find_prefix(self, root, prefix):
        node = root
        if not root.children:
            return False, 0

        for char in prefix:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break

            if char_not_found:
                return False, 0

        return True, node.counter


def run():
    root = TrieTree('*')
    root.add(root, 'mumumiya-umiko')
    root.add(root, 'hackson')
    pprint(root.find_prefix(root, 'mu'))
    pprint(root.find_prefix(root, 'hack'))
    pprint(root.find_prefix(root, 'ihack'))


if __name__ == '__main__':
    run()
