from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import Base

from sqlalchemy import Column, String, Integer, Boolean, Float

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    received_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # 函数名限定的, 因为继承了UserMixin，所以不必在此定义
    # def get_id(self):
    #     return self.id
    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 既不在礼物清单里，又不在愿望清单里，才可以添加
        gift = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wish = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gift and not wish:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))  # 查询主键，不用filter_by
