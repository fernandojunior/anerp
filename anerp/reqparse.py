from flask_restful.reqparse import Argument
from flask_restful.reqparse import RequestParser as OriginalRequestParser


class RequestParser(OriginalRequestParser):

    def __init__(self, *args, **kargs):
        arguments = kargs.pop('arguments', None)
        select = kargs.pop('select', None)
        update = kargs.pop('update', None)
        remove = kargs.pop('remove', None)
        super(RequestParser, self).__init__(*args, **kargs)
        if arguments:
            if select:  # add just selected arguments
                arguments = dict((k, arguments[k]) for k in select)
            self.add_arguments(arguments)
        if update:
            self.update_arguments(update)
        if remove:
            self.remove_arguments(remove)

    def add_arguments(self, arguments):
        '''Add arguments to be parsed. Accepts either a dictionary of arguments
        or a list of `Argument`.'''
        if isinstance(arguments, dict):  # {'argument': {'required': ...}, }
            arguments = [Argument(*i) for i in arguments.items()]
        for argument in arguments:
            self.add_argument(argument)

    def update_arguments(self, dictionary):
        ''' Update the arguments matching the given dictionary keys. '''
        for arg in self.args:
            if arg.name in dictionary.keys():
                setattr(arg, arg.name, dictionary[arg.name])

    def remove_arguments(self, names):
        ''' Remove the arguments matching the given names. '''
        for name in names:
            self.remove_argument(name)

    def copy(self, update=None, remove=None):
        ''' Creates a copy with the same set of arguments. '''
        parsercopy = super(RequestParser, self).copy()
        if update:
            parsercopy.update_arguments(update)
        if remove:
            parsercopy.remove_arguments(remove)
        return parsercopy
