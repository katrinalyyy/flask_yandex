from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')  # 1
def home():
    return render_template('index.html', title='Главная')


@main.route('/capacitor_page')  # 2
def capacitor_page():
    return render_template('capacitor_page.html')


@main.route('/blog')  # 3
def blog():
    return render_template('blog.html', title='Блог')   #&&&&&&&&&&


@main.route('/dielectric_page')  # 4
def dielectric_page():
    return render_template('dielectric_page.html')


@main.route('/formula_page')  # 5
def formula_page():
    return render_template('formula_page.html')


@main.route('/guides_page')  # 6
def guides_page():
    return render_template('guides_page.html')


@main.route('/notes_page')  # 7
def notes_page():
    return render_template('notes_page.html')


@main.route('/tickets_page')  # 8
def tickets_page():
    return render_template('tickets_page.html')


# @main.route('/account')  # 9
# def account():
#     return render_template('account.html')

#
# @main.route('/login')  # 11
# def login():
#     return render_template('login.html')

