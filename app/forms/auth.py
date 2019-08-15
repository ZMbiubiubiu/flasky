#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-11 11:01
# @Author  : bingo
# @Site    : 
# @File    : auth.py
# @Software: PyCharm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length, ValidationError, EqualTo

from app.models.user import User


class RegisterForm(Form):
    nickname = StringField(validators=[
        DataRequired(),
        Length(2, 10, message="昵称最少两个字符，最多十个字符")
    ])
    email = StringField(validators=[
        DataRequired(),
        Length(8, 64),
        Email(message='输入的邮箱格式不对')
    ])
    password = PasswordField(validators=[DataRequired(message="密码不可为空")])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已经被注册")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("昵称已经被注册")


class LoginForm(Form):
    email = StringField(validators=[
        DataRequired(),
        Length(8, 64),
        Email(message='输入的邮箱格式不对')
    ])
    password = PasswordField(validators=[DataRequired(message="密码不可为空")])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message="输入的邮箱格式不对")])


class ResetPasswordForm(Form):
    password1 = StringField(validators=[
        DataRequired(message="密码长度在需要在6-20个字符之间"),
        Length(6, 20),
        EqualTo('password2', message="两次输入的密码不同")
    ])
    password2 = StringField(validators=[
        DataRequired(),
        Length(6, 20)
    ])
