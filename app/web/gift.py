from flask import current_app, render_template, url_for, flash, redirect

from app.models.base import db
from app.models.gift import Gift
from app.spider.yushu import YuShuBook
from app.view_models.gift import MyGiftsViewModel
from app.web import web
from flask_login import login_required, current_user
# current_user 的信息来自 user 模型中的get_user函数的作用


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine ]
    wish_count_list = Gift.get_wish_count(isbn_list)
    my_gifts_view_model = MyGiftsViewModel(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=my_gifts_view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    # 验证isbn编号。首先格式对，然后对应书籍得存在
    # 一个用户不能同时赠送多本相同的书
    # 一个用户不能既赠送又索要同一本书
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id  # current_user就是一个实例化后的User模型
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash("这本书已经存在你的赠送清单或者愿望清单中，请不要重复添加")
    # 还是回到原来的页面，但是刷新了一次，没必要呀
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
