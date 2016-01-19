from flask import url_for, redirect

from ..blueprints import main


@main.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))
