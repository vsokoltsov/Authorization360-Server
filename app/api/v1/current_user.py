from flask_restful import Resource
from flask import request, g

from app.services.authorization import authenticate
from app.schemas.current_user import current_user_schema

class CurrentUserResource(Resource):
    """ Current User endpoint. """

    method_decorators = [authenticate]

    def get(self):
        return {'current_user': current_user_schema.dump(g.user).data }, 200
