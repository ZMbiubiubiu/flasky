from flask_login import login_user, logout_user

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.base import db
from app.models.user import User
from app.web import web
from flask import render_template, request, redirect, url_for, flash


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        # db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('?'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash("输入的用户名或密码错误")
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == "POST":
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            from app.libs.mail import send_mail
            send_mail(account_email, '重置你的密码',
                      'email/reset_password.html',
                      user=user, token=user.generate_token()
                      )
            flash("邮件已经发送，请注意查收")
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash("修改密码已成功")
            return redirect(url_for('web.login'))
        else:
            flash("重置密码失败")
    return render_template('auth/forget_password.html', form=form)

    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/register/confirm/<token>')
def confirm(token):
    pass
    # if current_user.confirmed:
    #     return redirect(url_for('main.index'))
    # if current_user.confirm(token):
    #     db.session.commit()
    #     flash('You have confirmed your account. Thanks!')
    # else:
    #     flash('The confirmation link is invalid or has expired.')
    # return redirect(url_for('main.index'))


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass
