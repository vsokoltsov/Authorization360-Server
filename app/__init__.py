import os

from flask import Flask

from .config import get_config_file
from app.api import api_v1_bp
from app.models import db
from app.commands.test import test

def create_app():
    """ Application factory. """

    app = Flask(__name__)
    app.config.from_object(get_config_file())
    db.init_app(app)
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
    app.cli.add_command(test)
    return app
