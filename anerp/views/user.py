# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from anerp.restful import Api, marshal_with, request_parser, Resource
from anerp.models.user import User

blueprint = Blueprint('user', __name__, static_folder='static')

api = Api(blueprint)


@blueprint.route('/list')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')

arguments = {
    'id': {'type': int, 'help': 'The user\'s id'},
    'username': {'help': 'The user\'s username'},
    'email': {'help': 'The user\'s email'},
    'password': {'help': 'The user\'s password'},
    'first_name': {'help': 'The user\'s first name'},
    'last_name': {'help': 'The user\'s last name'}}

patch_parser = request_parser(arguments, remove=['id'])  # create new parser

post_parser = request_parser(  # copy patch_parser
    patch_parser,
    update={  # update some arguments
        'username': {'required': True},
        'email': {'required': True},
        'password': {'required': True}},
    remove=['first_name', 'last_name'])

public_fields = User.marshal_fields(
    'id',
    'username',
    'email',
    'first_name',
    'last_name',
    'created_at')


@api.route('/<int:id>')
class UserApi(Resource):

    @marshal_with(public_fields)
    def get(self, id):
        return User.query.get_or_404(id)

    def patch(self, id):
        user = User.query.get_or_404(id)
        args = patch_parser.parse_args()
        for key, value in args.items():
            setattr(user, key, value)
        user.update()
        return self.get(id)

    def delete(self, id):
        user = User.query.get_or_404(id)
        user.delete()
        return '', 204


@api.route('/')
class UserList(Resource):

    @marshal_with(public_fields)
    def get(self):
        return User.query.all()

    @marshal_with(public_fields)
    def post(self):
        args = post_parser.parse_args()
        user = User.create(**args)
        return user
