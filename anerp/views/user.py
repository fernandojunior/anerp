# -*- coding: utf-8 -*-
'''User views.'''
from flask import Blueprint
from flask_restful import fields
from anerp.reqparse import RequestParser
from anerp.models.user import User
from anerp.restful import jsonify
from anerp.utils import Dictionary

Model = User

blueprint = Blueprint(Model.__name__, __name__, static_folder='static')

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

marshaller_fields = Dictionary({
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'full_name': fields.String,
    'active': fields.Boolean,
    'create_at': fields.DateTime(dt_format='iso8601')
})

marshallers = {
    'get': marshaller_fields()
}


@blueprint.route('/')
@blueprint.route('/<int:id>')
def get(id=None):
    data = Model.query.get_or_404(id) if id else Model.query.all()
    return jsonify(data, marshallers['get'])


@blueprint.route('/<int:id>', methods=['PATCH'])
def patch(id):
    obj = Model.query.get_or_404(id)
    args = RequestParser(arguments=request_parsers['patch']).parse()
    for key, value in args.items():
        setattr(obj, key, value)
    obj.update()
    return get(id)


@blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id):
    Model.query.get_or_404(id).delete()
    return '', 204


@blueprint.route('/', methods=['POST'])
def post():
    args = RequestParser(arguments=request_parsers['post']).parse()
    return get(Model.create(**args).id)
