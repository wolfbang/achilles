#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : consistent_hashing.py
# @Author: lucas
# @Date  : 1/4/19
# @Desc  :


from hashlib import md5
from bisect import bisect
from pprint import pprint
from string import letters


class Ring(object):
    def __init__(self, server_list, num_replicas=3):
        nodes = self.generate_nodes(server_list, num_replicas)
        hnodes = [self.hash(node) for node in nodes]
        hnodes.sort()

        self.server_list = server_list
        self.nodes = nodes
        self.hnodes = hnodes
        self.nodes_map = {self.hash(node): node.split("-")[1] for node in nodes}
        pass

    @staticmethod
    def hash(val):
        m = md5(val)
        return int(m.hexdigest(), 16)

    @staticmethod
    def generate_nodes(server_list, num_replicas):
        nodes = []
        for i in xrange(num_replicas):
            for server in server_list:
                nodes.append('{0}-{1}'.format(i, server))
        return nodes

    def get_node(self, val):
        pos = bisect(self.hnodes, self.hash(val))
        if pos == len(self.hnodes):
            return self.nodes_map[self.hnodes[0]]
        else:
            return self.nodes_map[self.hnodes[pos]]


def run():
    server_list = ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5', '127.0.0.6']
    ring = Ring(server_list)

    for letter in letters:
        pprint(ring.get_node(letter))


if __name__ == '__main__':
    run()
