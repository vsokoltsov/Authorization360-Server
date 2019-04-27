import os

from flask import Flask

from .config import get_config_file

application = Flask(__name__)
application.config.from_object(get_config_file())
