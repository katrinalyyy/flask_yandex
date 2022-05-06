import shutil
from flask import Blueprint, render_template, url_for, flash
from werkzeug.utils import redirect
from flask_login import current_user, logout_user, login_required

from blog import bcrypt, db
from blog.models import User
from blog.user.forms import RegistrationForm, LoginForm
import os

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.blog'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        full_path = os.path.join(os.getcwd(), 'blog/static', 'profile_pics', user.username)
        if not os.path.exists(full_path):
            os.mkdir(full_path)

        shutil.copy(f'{os.getcwd()}/blog/static/profile_pics/default.png', full_path)
        flash('Ваш аккаунт был создан. Вы можете войти на блог', 'Успех !!!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form, title='Регистрация', legend='Регистрация')


@users.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')  # gfdddddddddddddddddddd


@users.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html')


@users.route('/logout')
def logout():
    #
    db.session.commit()
    logout_user()
    return redirect(url_for('main.home'))
# @main.route('/')
# def home():
#     return render_template('index.html', title='Главная')
#
#
# @main.route('/capacitor_page')
# def capacitor_page():
#     return render_template('capacitor_page.html')
#
#
# @main.route('/blog')
# def blog():
#     return render_template('blog.html', title='Блог')
#
#
# @main.route('/dielectric_page')
# def dielectric_page():
#     return render_template('dielectric_page.html')
#
#
# @main.route('/formula_page')
# def formula_page():
#     return render_template('formula_page.html')
#
#
# @main.route('/guides_page')
# def guides_page():
#     return render_template('guides_page.html')
#
#
# @main.route('/notes_page')
# def notes_page():
#     return render_template('notes_page.html')
#
#
# @main.route('/tickets_page')
# def tickets_page():
#     return render_template('tickets_page.html')