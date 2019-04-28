from flask_restful import Resource, abort
from flask import request, g

from app.api import api_v1

from .authorization import AuthorizationResource
from .registration import RegistrationsResource

api_v1.add_resource(AuthorizationResource, '/sign_in')
api_v1.add_resource(RegistrationsResource, '/sign_up')
