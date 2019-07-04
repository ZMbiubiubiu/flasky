from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationships


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey='user.id')  # 上一行的user
    # book 的信息没有存储到数据库中.所以没必要如此.那么该如何关联上呢?
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey='book.id')
    isbn = Column(String(20), nullable=False)
    launched = Column(Boolean, default=False)   # 默认书没有被送出去
