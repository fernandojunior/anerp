from flask import Blueprint, redirect, url_for


blueprint = Blueprint('main', __name__, static_folder='static')


@blueprint.route('/')
def home():
    return redirect(url_for('static', filename='index.html'))
