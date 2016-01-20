from flask import Blueprint
from anerp.restful import Resource, Api

blueprint = Blueprint('helloworld', __name__, static_folder='static')

api = Api(blueprint)


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world' + __name__}
