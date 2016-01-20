# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from anerp.restful import Api, Resource, parse
from anerp.models.user import User

blueprint = Blueprint('user', __name__, static_folder='static')

api = Api(blueprint)


@blueprint.route('/list')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')


from flask_restful import fields, marshal_with
from flask_restful.reqparse import Argument

user_arguments = [
    Argument('username', required=True, help='The user\'s username'),
    Argument('email', required=True, help='The user\'s email'),
    Argument('password', required=True, help='The user\'s password'),
    Argument('first_name', help='The user\'s first name'),
    Argument('last_name', help='The user\'s last name')
]


# user_arguments2 = dict(
#     username={'required': True, 'help': 'The user\'s username'},
#     email={'required': True, 'help': 'The user\'s email'},
#     password={'required': True, 'help': 'The user\'s password'},
#     first_name={'help': 'The user\'s first name'},
#     last_name={'help': 'The user\'s last name'})

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String}


@api.route('/<int:id>')
class UserApi(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        return User.query.get_or_404(id)

    def patch(self, id):
        user = User.query.get_or_404(id)
        args = parse('*', user_arguments)
        print(type(args))
        print(dir(args))
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

    @marshal_with(user_fields)
    def get(self):
        return User.query.all()

    @marshal_with(user_fields)
    def post(self):
        args = parse('username email password', user_arguments)
        user = User.create(args.username, args.email, args.password)
        return user
