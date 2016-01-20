# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
import flask_restful as restful

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
