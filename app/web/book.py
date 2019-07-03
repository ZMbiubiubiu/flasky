"""
2019年 06月 11日 星期二 16:02:55 CST

"""
from flask import jsonify, request
from app.view_models.book import BookCollection
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu import YuShuBook
from . import web
import json


@web.route('/book/search')
def search():
    """\
        ?q=金庸&page=1
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()   # 去掉空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'key':
            yushu_book.search_by_key(q, page)
        else:
            yushu_book.search_by_isbn(q)
        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)