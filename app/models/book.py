"""
2019年 06月 13日 星期四 13:06:34 CST
"""
from sqlalchemy import Column, Integer, String

from app.models.base import db, Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), nullable=True, default="未名")
    price = Column(String(20))
    binding = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(20), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass


