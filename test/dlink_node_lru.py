#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-29 14:25
# @Author  : bingo
# @Site    : 
# @File    : dlink_node_lru.py
# @Software: PyCharm


class DLinkedNode:
    def __int__(self, key=0):
        self.key = 0
        self.prev = None
        self.next = None


class LRUCache:


    def _add_node(self, node):
        """总是添加到开头"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self):
        tail = self.tail.prev
        tail.prev.next = self.tail
        self.tail.prev = tail.prev
        return tail

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(key=-1), DLinkedNode(key=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = DLinkedNode(key=key)
        # node = DLinkedNode()
        self._move_to_head(node)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """秘钥已经在LRU缓存中的时候"""
        if key in self.cache:
            self.cache[key] = value
        # 没在缓存中
        if self.size == self.capacity:
            self._pop_tail()
        node = DLinkedNode(key=key)
        # node = DLinkedNode()
        self._add_node(node)
        self.size += 1
        self.cache[key] = value


if __name__ == "__main__":
    lru = LRUCache(2)
    print(lru.cache)

    print(lru.get(1))
    lru.put(1, 2)
    # lru.put(3, 4)
    # lru.put(4, 5)
    # lru.get(1)
