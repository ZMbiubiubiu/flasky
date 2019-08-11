from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # 将Base设置成基类，而不是创建一个Base的表
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)  # 默认值为1, 表示未删除

    def __init__(self):
        # Base.create_time
        pass

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if key != 'id' and hasattr(self, key):
                setattr(self, key, value)
