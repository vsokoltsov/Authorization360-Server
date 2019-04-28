import os
import sys

def get_config_file():
    """ Get config file path based on the environment. """

    default_config_class = 'Config'
    flask_env = os.environ.get('FLASK_ENV', default_config_class)
    try:
        return getattr(sys.modules[__name__], f'{flask_env.capitalize()}Config')
    except AttributeError:
        return Config

def get_database_path():
    """ Set default database path based on environment variables. """

    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    database = os.environ.get('POSTGRES_DB')
    return f'postgresql+psycopg2://{user}:{password}@authorization360_db/{database}'


class Config():
    """ Base config class. """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_database_path()

class DevelopmentConfig(Config):
    """ Config for development environment. """
    pass

class TestConfig(Config):
    """ Config for test environment. """
    pass
