# -*- coding: utf-8 -*-
'''Application configuration.'''
import os


class Config(object):
    '''Base configuration.'''

    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'secret-key')  # TODO
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    CACHE_TYPE = 'simple'  # Can be 'memcached', 'redis', etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True  # reqparse error handling


class ProdConfig(Config):
    '''Production configuration.'''

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO


class DevConfig(Config):
    '''Development configuration.'''

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    CACHE_TYPE = 'simple'  # Can be 'memcached', 'redis', etc.


class TestConfig(Config):
    '''Test configuration.'''

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4
    WTF_CSRF_ENABLED = False  # Allows form testing
