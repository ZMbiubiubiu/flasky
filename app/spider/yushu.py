"""
2019年 06月 11日 星期二 15:53:30 CST
"""

from flask import current_app  # 指代的就是当前的核心app对象
from app.libs.http_method import HTTP


class YuShuBook:
    # 一个类要有特征(类变量/实例变量)和行为(方法)
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []  # 真正的书籍数据

    def search_by_isbn(self, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_key(self, keyword, page=1):

        url = YuShuBook.key_url.format(keyword, current_app.config['PER_PAGE'],
                                 self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page-1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

