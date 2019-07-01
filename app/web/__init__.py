"""
2019年 06月 13日 星期四 09:33:31 CST
"""
from flask import Blueprint

web = Blueprint('web', __name__)


from . import book
from . import user
