"""
2019年 06月 11日 星期二 16:02:55 CST

"""
from flask import jsonify
from fisher import app
from helper import is_isbn_or_key
from yushu import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q: object, page: object) -> object:
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'key':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_key(q)
    return jsonify(result)