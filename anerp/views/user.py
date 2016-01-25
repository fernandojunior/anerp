# -*- coding: utf-8 -*-
'''User views.'''
from flask_restful import fields
from anerp.utils import Dictionary
from anerp.restful import Api
from anerp.models.user import User


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

api = Api(User, request_parsers, marshaller)
blueprint = api.app
