"""

"""

from flask import Flask, current_app

app = Flask(__name__)

ctx = app.app_context() # 离线应用/单元测试
ctx.push()

a = current_app
d = current_app.config['DEBUG']

ctx.pop()


