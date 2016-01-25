# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask
from .ext import bcrypt, cache, db, login_manager, \
    migrate
from .libs.restful import register_api
from .views import main, user


def create_app(config):
    '''An application factory, as explained in
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    register_apis(app)
    return app


def register_extensions(app):
    '''Register Flask extensions.'''
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    '''Register Flask blueprints.'''
    app.register_blueprint(main.blueprint, url_prefix='/')
    return None


def register_apis(app):
    register_api(user, app, url_prefix='/users', static_folder='static')
