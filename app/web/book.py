"""
2019年 06月 11日 星期二 16:02:55 CST

"""
from flask import jsonify, request
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """\
        ?q=金庸&page=1
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()   # 去掉空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_key(q)
        else:
            result = YuShuBook.search_by_isbn(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)