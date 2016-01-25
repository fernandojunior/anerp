# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import sys
from flask import flash


"""Python 2/3 compatibility module."""
if int(sys.version[0]) == 2:
    text_type = unicode  # noqa
    binary_type = str
    string_types = (str, unicode)  # noqa
    unicode = unicode  # noqa
    basestring = basestring  # noqa
else:
    text_type = str
    binary_type = bytes
    string_types = (str,)
    unicode = str
    basestring = (str, bytes)


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for e in errors:
            flash('{}:{}'.format(getattr(form, field).label.text, e), category)


class Dictionary(dict):

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

    def update(self, elements):
        '''Update the elements of this namespace with new values.'''
        for k, v in elements.items():
            if k in self.keys():
                if isinstance(self[k], dict):
                    for kv, vv in v.items():
                        self[k][kv] = vv
                else:
                    self[k] = v

    def copy(self, *args):
        '''Create new one with selected keys.'''
        copy = dict((k, self[k]) for k in args) if args else dict(self)
        return self.__class__(copy)

    def remove(self, *args):
        '''Removes matching keys.'''
        for key in args:
            del self[key]

    def __call__(self, select=None, update=None, remove=None):
        obj = self.copy(*select) if select else self.copy()
        if update:
            obj.update(update)
        if remove:
            obj.remove(remove)
        return obj
