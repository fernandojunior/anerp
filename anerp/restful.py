# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
from flask import Blueprint, jsonify
from flask_restful import marshal
from anerp.reqparse import RequestParsers


def jsonify_with_marshal(data, marshaller):
    return jsonify(data=marshal(data, marshaller))


def register_api(module, app, **options):
    attrs = {
        '__model__': module.__model__,
        'marshaller': module.marshaller,
        'request_arguments': module.request_arguments,
        'request_parsers': module.request_parsers
    }
    cls = type(module.__name__ + 'API', (API,), attrs)
    cls.init_app(app, **options)


class API:

    __model__ = None

    request_parsers = None

    marshaller = None

    url_rules = {
        '/': ['get', 'post'],
        '/<int:id>': ['get', 'patch', 'delete'],
    }

    def __init__(self, **options):
        self.request_parsers = RequestParsers(self.request_parsers)
        self.blueprint = Blueprint(self.model.__name__, __name__, **options)
        self.init_url_rules()

    @classmethod
    def init_app(cls, app, **options):
        app.register_blueprint(cls().blueprint, **options)

    def add_url_rule(self, rule, fn):
        if isinstance(fn, str):
            fn = getattr(self, fn)
        name = fn.__name__
        self.blueprint.add_url_rule(rule, name, fn, methods=[name.upper()])

    def init_url_rules(self):
        for rule, views in self.url_rules.items():
            for view in views:
                self.add_url_rule(rule, view)

    @property
    def model(self):
        return self.__model__

    def get(self, id=None):
        obj = self.model.query.get_or_404(id) if id else self.model.query.all()
        return jsonify_with_marshal(obj, self.marshaller)

    def patch(self, id):
        obj = self.model.query.get_or_404(id)
        args = self.request_parsers('patch')
        for key, value in args.items():
            setattr(obj, key, value)
        obj.update()
        return self.get(id)

    def delete(self, id):
        self.model.query.get_or_404(id).delete()
        return '', 204

    def post(self):
        obj = self.model.create(**self.request_parsers('post'))
        return self.get(obj.id)
