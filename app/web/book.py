"""
2019年 06月 11日 星期二 16:02:55 CST

"""
from flask import jsonify, request, render_template, flash
from app.view_models.book import BookCollection, BookViewModel
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
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('您输入的查询字符串不符, 请在检查一下')
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {
        'name': 'ZzLee',
        'age': 25,
    }
    flash('hello world')
    flash('hello world')
    flash('hello world')
    flash('hello world')

    return render_template('test.html', data=r)