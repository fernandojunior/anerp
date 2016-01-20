# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
import flask_restful as restful
from flask_restful.reqparse import Argument, RequestParser

# Alias common Flask-RESTful names
Resource = restful.Resource


class Api(restful.Api):

    def route(self, *args, **kwargs):
        """
        Routing via decorators: http://flask.pocoo.org/snippets/129/
        """
        def wrapper(cls):
            self.add_resource(cls, *args, **kwargs)
            return cls
        return wrapper


def create_parser(select, arguments, sep=' '):
    parser = RequestParser()

    if isinstance(select, str) and select != '*':
        select = select.split(sep)

    if isinstance(arguments, dict):
        for name, values in arguments.items():
            if select == '*' or name in select:
                parser.add_argument(name, values)
        return parser

    for argument in arguments:
        if select == '*' or argument.name in select:
            parser.add_argument(argument)

    return parser


def parse(select, arguments):
    return create_parser(select, arguments).parse_args()
