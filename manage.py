#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Management script.'''
import os

from flask_migrate import MigrateCommand
from flask_script import Manager, Server, Shell
from flask_script.commands import ShowUrls

from anerp.app import create_app
from anerp.lib.database import db
from anerp.models.user import User
from anerp.settings import DevConfig, ProdConfig

CONFIG = ProdConfig if os.environ.get('ANERP_ENV') == 'prod' else DevConfig
app = create_app(CONFIG)
manager = Manager(app)


def _make_context():
    '''
    Return context dict for a shell session so you can access app, db, and the
    User model by default.
    '''
    return {'app': app, 'db': db, 'User': User}

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('urls', ShowUrls())

if __name__ == '__main__':
    manager.run()
