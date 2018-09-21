#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aho_corasick_automaton.py
# @Author: lucas
# @Date  : 9/21/18
# @Desc  :

from pprint import pprint


class TrieNode(object):
    __slot__ = ['value', 'next', 'fail', 'emit']

    def __init__(self, value):
        self.value = value
        self.next = dict()
        self.fail = None
        self.emit = None


class AhoCorasick(object):
    __slots__ = ['_root']

    def __init__(self, words):
        self._root = AhoCorasick._build_trie(words)

    @staticmethod
    def _build_trie(words):
        assert isinstance(words, list) and words
        root = TrieNode('root')
        for word in words:
            node = root
            for c in word:
                if c not in node.next:
                    node.next[c] = TrieNode(c)

                node = node.next[c]

            if not node.emit:
                node.emit = {word}
            else:
                node.emit.add()

        queue = []
        queue.insert(0, (root, None))
        while len(queue) > 0:
            node_parent = queue.pop()
            curr, parent = node_parent[0], node_parent[1]
            for sub in curr.next.values():
                queue.insert(0, (sub, curr))

            if parent is None:
                continue

            elif parent is root:
                curr.fail = root

            else:
                fail = parent.fail
                while fail and curr.value not in fail.next:
                    fail = fail.fail

                if fail:
                    curr.fail = fail.next[curr.value]
                    pass
                else:
                    curr.fail = root

        return root

    def search(self, s):
        seq_list = []
        node = self._root
        for i, c in enumerate(s):
            match = True
            while c not in node.next:
                if not node.fail:
                    match = False
                    node = self._root
                    break
                node = node.fail
            if not match:
                continue
            node = node.next[c]
            if node.emit:
                for _ in node.emit:
                    from_index = i + 1 - len(_)
                    match_info = (from_index, _)
                    seq_list.append(match_info)

                node = self._root

        return seq_list


if __name__ == '__main__':
    aho = AhoCorasick(['ass', 'noo'])
    pprint(aho.search('hasnoassexpirenoothoass'))
