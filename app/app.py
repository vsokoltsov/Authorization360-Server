import os

from flask import Flask

from .config import get_config_file
from app.api import api_v1_bp

application = Flask(__name__)
application.config.from_object(get_config_file())
application.register_blueprint(api_v1_bp, url_prefix='/api/v1')
