# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
from datetime import datetime
import flask_restful as restful
from flask_restful import fields

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
