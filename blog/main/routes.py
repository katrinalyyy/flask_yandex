from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('index.html', title='Главная')


@main.route('/capacitor_page')
def capacitor_page():
    return render_template('capacitor_page.html')


@main.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')


@main.route('/dielectric_page')
def dielectric_page():
    return render_template('dielectric_page.html')


@main.route('/formula_page')
def formula_page():
    return render_template('formula_page.html')


@main.route('/guides_page')
def guides_page():
    return render_template('guides_page.html')


@main.route('/notes_page')
def notes_page():
    return render_template('notes_page.html')


@main.route('/tickets_page')
def tickets_page():
    return render_template('tickets_page.html')
