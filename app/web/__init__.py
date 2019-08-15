"""
2019年 06月 13日 星期四 09:33:31 CST
"""
from flask import Blueprint, render_template

web = Blueprint('web', __name__, template_folder='templates')


@web.app_errorhandler(404)
def not_fount(e):
    return render_template('404.html'), 404


# 导入执行
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
