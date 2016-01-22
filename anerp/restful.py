# -*- coding: utf-8 -*-
"""
RESTFul module.
"""
from datetime import datetime
from flask import jsonify as original_jsonify
from flask_restful import fields, marshal


type_mapper = {
    str: fields.String,
    datetime: fields.DateTime(dt_format='iso8601'),
    float: fields.Float,
    int: fields.Integer,
    bool: fields.Boolean}
# TODO: FormattedString Url Arbitrary Nested List Raw Fixed Price


def create_marshaller(keys, types):
    '''Create fields based on default Python types to use with marshal'''
    return {k: type_mapper[v] for k, v in zip(keys, types)}


def jsonify(data, marshaller=None):
    if marshaller:
        data = marshal(data, marshaller)
    return original_jsonify(data=data)
