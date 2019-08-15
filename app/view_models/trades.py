#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-14 14:33
# @Author  : bingo
# @Site    : 
# @File    : trades.py
# @Software: PyCharm

class TradeInfo:
    def __init__(self, items):
        self.total = 0
        self.trades = []
        self.__parse(items)

    def __parse(self, items):
        self.total = len(items)
        self.trades = [self.__map_to_trade(item) for item in items]

    def __map_to_trade(self, item):
        if item.create_datetime:
            time = item.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            username=item.user.nickname,
            time=time,
            id=item.id

        )
