# -*- coding: utf-8 -*-
'''User views.'''
from anerp.libs.marshal import fields
from anerp.utils import Dictionary
from anerp.models.user import User

__model__ = User

marshaller = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'full_name': fields.String,
    'active': fields.Boolean,
    'create_at': fields.DateTime(dt_format='iso8601')
}

request_arguments = Dictionary({
    'username': {'help': 'The user\'s username'},
    'email': {'help': 'The user\'s email'},
    'password': {'help': 'The user\'s password'},
    'first_name': {'help': 'The user\'s first name'},
    'last_name': {'help': 'The user\'s last name'}})

request_parsers = {
    'patch': request_arguments(),
    'post': request_arguments(
        select=('username', 'email', 'password'),
        update={
            'username': {'required': True},
            'email': {'required': True},
            'password': {'required': True}
        }
    )
}
