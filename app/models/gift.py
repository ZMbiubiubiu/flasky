from flask import current_app

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationship

from app.spider.yushu import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)  # 上一行的user
    # book 的信息没有存储到数据库中.所以没必要如此.那么该如何关联上呢?
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey='book.id')
    isbn = Column(String(20), nullable=False)
    launched = Column(Boolean, default=False)  # 默认书没有被送出去

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(launched=False, uid=uid).order_by(
            desc(Gift.create_time)
        ).all()

        return gifts

    def get_wish_count(isbn_list):
        from app.models.wish import Wish
        """
        target: 根据传入的一组isbn，到wish表看每一个isbn对应的wish记录的心愿数，返回各个分组的数量
        method：filter 与 filter_by 的区别：filter_by 接受关键字参数，filter 接受表达式
        :return:
        """
        # 涉及到跨表查询
        count_list = db.session.query(Wish.isbn, func.count(Wish.id)).filter(
            Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1,
        ).group_by(
            Wish.isbn
        ).all()
        # 最好别返回一个元组列表
        count_list = [{'isbn': i[0], 'count': i[1]} for i in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 一个Gift实例表示数据库的一条记录，而此方法可以返回多条记录，感觉有点别扭
    # 所以将其写成类方法
    @classmethod
    def recent(cls):
        """
            链式调用：一个主体，多个子函数
            主体：在这里就是Query实例
            子函数：在这里就是filter_by,order_by,limit等函数。
            子函数的特点：每个子函数的返回值都是Query实例（所以才能够链式调用哦）
        """
        # TODO 没有去重 .group_by(Gift.isbn)
        recent_gifts = Gift.query.filter_by(launched=False).order_by(
            desc(Gift.create_time)
        ).limit(
            current_app.config['RECENT_BOOK_COUNT']
        ).all()

        return recent_gifts
