#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 17:12
# @Author  : bingo
# @Site    : 
# @File    : gift.py
# @Software: PyCharm
from collections import namedtuple

from app.view_models.book import BookViewModel


# MyGiftViewModel = namedtuple('MyGiftViewModel', 'id', 'book', 'wish_count')
# 为了支持序列化，这里还是采用字典

class MyGiftsViewModel:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            # 优化双层嵌套，就是内层循环函数化（代码大全）
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['isbn']
        my_gift = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        # my_gift = MyGiftViewModel(gift.id, BookViewModel(gift.book), count)
        return my_gift
