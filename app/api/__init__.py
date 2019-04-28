from flask_restful import Api
from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)

from .v1 import *
