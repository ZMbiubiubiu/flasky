"""
2019年 06月 11日 星期二 15:53:30 CST
"""

from http_method import HTTP


class YuShuBook:
    isbn_url = ''
    key_url = ''

    def search_by_isbn(self, isbn):
        r = HTTP.get(YuShuBook.isbn_url)
        return 'isbn'

    def search_by_key(self, key):
        r = HTTP.get(YuShuBook.key_url)
        return 'key'