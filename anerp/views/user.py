# -*- coding: utf-8 -*-
'''User views.'''
from flask import Blueprint
from anerp.reqparse import RequestParser
from anerp.models.user import User
from anerp.restful import jsonify

Model = User

blueprint = Blueprint(Model.__name__, __name__, static_folder='static')

arguments = {
    'id': {'type': int, 'help': 'The user\'s id'},
    'username': {'help': 'The user\'s username'},
    'email': {'help': 'The user\'s email'},
    'password': {'help': 'The user\'s password'},
    'first_name': {'help': 'The user\'s first name'},
    'last_name': {'help': 'The user\'s last name'}}

patch_parser = RequestParser(arguments=arguments, remove=['id'])

post_parser = patch_parser.copy(
    update={
        'username': {'required': True},
        'email': {'required': True},
        'password': {'required': True}},
    remove=['first_name', 'last_name'])

marshaller = Model.create_marshaller(
    'id',
    'username',
    'email',
    'first_name',
    'last_name',
    'created_at')


@blueprint.route('/')
@blueprint.route('/<int:id>')
def get(id=None):
    data = Model.query.get_or_404(id) if id else Model.query.all()
    return jsonify(data, marshaller)


@blueprint.route('/<int:id>', methods=['PATCH'])
def patch(id):
    obj = Model.query.get_or_404(id)
    args = patch_parser.parse_args()
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
    args = post_parser.parse_args()
    return get(Model.create(**args).id)
