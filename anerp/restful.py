# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
from datetime import datetime
import flask_restful as restful
from flask_restful import fields
from flask_restful.reqparse import Argument, RequestParser

# Alias common Flask-RESTful names
Resource = restful.Resource
marshal_with = restful.marshal_with


class Api(restful.Api):

    def route(self, *args, **kwargs):
        '''Routing via decorators: http://flask.pocoo.org/snippets/129/'''
        def wrapper(cls):
            self.add_resource(cls, *args, **kwargs)
            return cls
        return wrapper


def request_parser(*args, **kargs):
    '''Create or copy a request parser.'''
    if isinstance(args[0], RequestParser):
        return copy_request_parser(*args, **kargs)
    else:
        return create_request_parser(*args, **kargs)


def create_request_parser(arguments, select='*', update=None, remove=None):
    '''Create a request parser with arguments.'''
    parser = RequestParser()

    if isinstance(arguments, dict):  # {'argument': {'required': True, ...}, }
        arguments = [Argument(k, v) for k, v in arguments.items()]

    for argument in arguments:  # Argument list
        if select == '*' or argument.name in select:
            parser.add_argument(argument)

    if update:
        update_request_parser(parser, update)

    if remove:
        remove_parser_arguments(parser, remove)

    return parser


def copy_request_parser(parser, update=None, remove=None):
    '''Copy a request parser. Arguments can be updated or removed.'''
    parsercopy = parser.copy()
    if update:
        update_request_parser(parsercopy, update)
    if remove:
        remove_parser_arguments(parsercopy, remove)
    return parsercopy


def update_request_parser(parser, arguments):
    '''Update request parser arguments.'''
    for arg in parser.args:
        if arg.name in arguments.keys():
            setattr(arg, arg.name, arguments[arg.name])


def remove_parser_arguments(parse, arguments):
    '''Remove request parser arguments.'''
    for argument in arguments:
        parse.remove_argument(argument)


def parse_request(arguments, select='*'):
    '''Parse selected request arguments based on a list of arguments.'''
    return create_request_parser(arguments, select).parse_args()


type_mapper = {
    str: fields.String,
    datetime: fields.DateTime(dt_format='iso8601'),
    float: fields.Float,
    int: fields.Integer,
    bool: fields.Boolean}
# TODO: FormattedString Url Arbitrary Nested List Raw Fixed Price


def create_marshal_fields(keys, types):
    '''Create fields based on default Python types to use with marshal'''
    return {k: type_mapper[v] for k, v in zip(keys, types)}
