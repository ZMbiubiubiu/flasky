"""
2019年 06月 13日 星期四 09:33:31 CST
"""
from flask import Blueprint

web = Blueprint('web', __name__)

# 导入执行
from app.web import book
# from . import user
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
