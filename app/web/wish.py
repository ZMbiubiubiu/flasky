from flask import flash, render_template, url_for, redirect

from app.models.base import db
from app.models.wish import Wish
from app.view_models.wish import MyWishesViewModel
from app.web import web
from flask_login import login_required, current_user


@web.route('/my/wishes')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_mine]
    gift_count_list = Wish.get_gift_count(isbn_list)
    my_wish_view_model = MyWishesViewModel(wishes_of_mine, gift_count_list)
    return render_template('my_wishes.html', wishes=my_wish_view_model.wishes)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已经存在你的赠送清单或者愿望清单中，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/wishes/<wid>/redraw')
def redraw_from_wishes(wid):
    pass
