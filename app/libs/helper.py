"""
    2019年 06月 11日 星期二 13:00:02 CST
    __author__ : ZzLee
"""

def is_isbn_or_key(word):
    """
        判断关键字查询还是isbn查询
    """
    isbn_or_key = 'key' # 默认为关键字查询
    if len(word) == 13 and word.isdigit():  # isbn13 的标准
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():  # isgn10 的标准
        isbn_or_key = 'isbn'
    return isbn_or_key
