#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-11 22:51
# @Author  : bingo
# @Site    : 
# @File    : ctx.py
# @Software: PyCharm

from contextlib import contextmanager


@contextmanager
def book_mark():
    print('<', end='')
    yield
    print('>')


with book_mark():
    print('射雕英雄传', end='')
