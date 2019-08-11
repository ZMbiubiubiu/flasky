#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-29 14:07
# @Author  : bingo
# @Site    : 
# @File    : order_dict.py
# @Software: PyCharm


from collections import OrderedDict


class LRUCache:
    """实现LRU缓存"""

    def __init__(self, capacity: int):
        self._order_dict = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        self._move_to_end_if_exist(key)
        return self._order_dict.get(key, -1)

    def put(self, key: int, value: int) -> None:
        self._move_to_end_if_exist(key)
        self._order_dict[key] = value
        if len(self._order_dict) > self._capacity:
            self._order_dict.popitem(last=False)

    def _move_to_end_if_exist(self, key):
        if key in self._order_dict:
            self._order_dict.move_to_end(key)


