#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-03 18:34
# @Author  : bingo
# @Site    : 
# @File    : test_current_app.py
# @Software: PyCharm
from flask import Flask, current_app

app = Flask(__name__)


with app.app_context():
    a = current_app
print('hello')





