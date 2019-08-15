#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-11 17:44
# @Author  : bingo
# @Site    : 
# @File    : wish.py
# @Software: PyCharm
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from app.spider.yushu import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)  # 上一行的user
    # book 的信息没有存储到数据库中.所以没必要如此.那么该如何关联上呢?
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey='book.id')
    isbn = Column(String(20), nullable=False)
    launched = Column(Boolean, default=False)  # 默认书没有被送出去

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(launched=False, uid=uid).order_by(
            desc(Wish.create_time)
        ).all()

        return wishes

    def get_gift_count(isbn_list):
        from app.models.gift import Gift
        """
        target: 根据传入的一组isbn，到wish表看每一个gift对应的记录的心愿数，返回各个分组的数量
        method：filter 与 filter_by 的区别：filter_by 接受关键字参数，filter 接受表达式
        :return:
        """
        # 涉及到跨表查询
        count_list = db.session.query(Gift.isbn, func.count(Wish.id)).filter(
            Gift.launched == False, Gift.isbn.in_(isbn_list), Gift.status == 1,
        ).group_by(
            Gift.isbn
        ).all()
        # 最好别返回一个元组列表
        count_list = [{'isbn': i[0], 'count': i[1]} for i in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
