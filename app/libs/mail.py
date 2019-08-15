#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-15 14:48
# @Author  : bingo
# @Site    : 
# @File    : email.py
# @Software: PyCharm
from flask import current_app, render_template, flash

from app import mail
from flask_mail import Message

import threading


def send_async_mail(app, msg):
    # 构建应用上下文
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('邮件测试', sender='390047718@qq.com',
    #               body = '数城未来实习', recipients=['390047718@qq.com']
    #               )
    msg = Message('[鱼书] ' + subject,  # 邮件标题
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to]  # 邮件接收者
                  )
    msg.html = render_template(template, **kwargs)
    # flask 核心对象，而非代理对象LocalProxy
    app = current_app._get_current_object()
    t = threading.Thread(target=send_async_mail, args=[app, msg])
    t.start()
