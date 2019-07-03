"""
2019年 06月 12日 星期三 16:42:58 CST
"""
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__, static_folder='static')  # 这个__name__决定了我们这个应用的根目录是app,而不是flasky
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)