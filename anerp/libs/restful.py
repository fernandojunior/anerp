# -*- coding: utf-8 -*-
'''
RESTFul module.
'''
from flask import Blueprint, jsonify
from anerp.libs.marshal import marshal
from anerp.libs.reqparse import RequestParsers


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

    url_rules = [
        ('/fields', 'getfields', {'methods': ['GET']})
    ]

    def __init__(self, **options):
        self.request_parsers = RequestParsers(self.request_parsers)
        self.blueprint = Blueprint(self.model.__name__, __name__, **options)
        self.init_default_url_rules()
        self.init_url_rules()

    @classmethod
    def init_app(cls, app, **options):
        app.register_blueprint(cls().blueprint, **options)

    def add_url_rule(self, rule, view_func, **options):
        if isinstance(view_func, str):
            view_func = getattr(self, view_func)
        endpoint = view_func.__name__
        method = endpoint.split('_')[0].upper()
        options['methods'] = options.get('methods', [method])
        self.blueprint.add_url_rule(rule, endpoint, view_func, **options)

    def init_default_url_rules(self):
        self.add_url_rule('/', self.get)
        self.add_url_rule('/<int:id>', self.get)
        self.add_url_rule('/<int:id>', self.patch)
        self.add_url_rule('/<int:id>', self.delete)
        self.add_url_rule('/', self.post)

    def init_url_rules(self):
        for each in self.url_rules:
            self.add_url_rule(each[0], each[1], **each[2])

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

    def getfields(self):
        data = dict((k, str(v)) for k, v in self.marshaller.items())
        return jsonify(data=data)
