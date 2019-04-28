from app.api import api_v1
from flask_restful import Resource, abort

from .authorization import AuthorizationResource

api_v1.add_resource(AuthorizationResource, '/authorizations')