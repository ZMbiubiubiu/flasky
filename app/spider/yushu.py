"""
2019年 06月 11日 星期二 15:53:30 CST
"""

from flask import current_app
from app.libs.http_method import HTTP


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_key(cls, keyword, page=1):

        url = cls.key_url.format(keyword, current_app.config['PER_PAGE'],
                                 cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']

