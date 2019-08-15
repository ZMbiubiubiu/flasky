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

class MyWishesViewModel:
    def __init__(self, wishes_of_mine, gift_count_list):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine
        self.__gift_count_list = gift_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            # 优化双层嵌套，就是内层循环函数化（代码大全）
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes

    def __matching(self, wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['isbn']
        my_wish = {
            'wishes_count': count,
            'book': BookViewModel(wish.book),
            'id': wish.id
        }
        # my_gift = MyGiftViewModel(gift.id, BookViewModel(gift.book), count)
        return my_wish

