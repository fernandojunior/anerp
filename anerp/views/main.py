from flask import Blueprint, url_for, redirect


blueprint = Blueprint('main', __name__, static_folder='static')


@blueprint.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))
