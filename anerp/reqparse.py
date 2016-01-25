from flask_restful.reqparse import Argument
from flask_restful.reqparse import RequestParser as OriginalRequestParser
from anerp.utils import Dictionary


class RequestParser(OriginalRequestParser):

    def __init__(self, *args, **kargs):
        arguments = kargs.pop('arguments', None)
        super(RequestParser, self).__init__(*args, **kargs)
        if arguments:
            self.add_arguments(arguments)

    def add_arguments(self, arguments):
        '''Add arguments to be parsed. Accepts either a dictionary of arguments
        or a list of `Argument`.'''
        if isinstance(arguments, dict):  # {'argument': {'required': ...}, }
            arguments = [Argument(*i) for i in arguments.items()]
        for argument in arguments:
            self.add_argument(argument)

    def parse(self, *args, **kwargs):
        '''`parse_args` alias.'''
        return self.parse_args(*args, **kwargs)


class RequestParsers(Dictionary):

    def __init__(self, parsers):
        '''
        Create a `RequestParser` dictionary from a mapping object's
            (name, arguments) pairs.
        '''
        self.parsers = {}
        for name, arguments in parsers.items():
            self.parsers[name] = RequestParser(arguments=arguments)

    def __call__(self, name):
        '''Parse a request parse with given name.'''
        return self.parsers[name].parse()
