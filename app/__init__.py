import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from dotenv import find_dotenv

from .config import get_config_file, get_database_path
from app.api import api_v1_bp
from app.models import db
from app.commands.test import test
from app.utils.db import run_migrations
from app.utils.routes import utils


def _init_db(app):
    """ Initialize database with all necessary attributes """

    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_path()
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    if os.environ.get('FLASK_ENV') != 'test':
        run_migrations()

def create_app():
    """ Application factory. """

    if os.environ.get('PLATFORM') == 'GCP':
        load_dotenv(find_dotenv('.env.production'))

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(get_config_file())
    _init_db(app)
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
    app.register_blueprint(utils, url_prefix='/utils')
    app.cli.add_command(test)
    return app

app = create_app()
