from datetime import datetime

# 继承关系 BaseQuery(flask_sqlalchemy) 继承自 Query(sqlalchemy)
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    """
        为了实现数据库的软删除，需要重写filter_by函数
        同样找个机会，让我们的查询能够使用这个重写的类
    """

    def filter_by(self, **kwargs):
        if 'status' not in kwargs:
            kwargs['status'] = 1
        # 之所以有return，是因为原来的filter_by 就是有返回值的
        return super().filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True  # 将Base设置成基类，而不是创建一个Base的表
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)  # 默认值为1, 表示未删除

    def __init__(self):
        # Base.create_time
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if key != 'id' and hasattr(self, key):
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
