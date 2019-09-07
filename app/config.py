import os
import sys
import sqlalchemy

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

    host = os.environ.get('POSTGRES_HOST', '').strip()
    user = os.environ.get('POSTGRES_USER', '').strip()
    password = os.environ.get('POSTGRES_PASSWORD', '').strip()
    database = os.environ.get('POSTGRES_DB', '').strip()
    url = sqlalchemy.engine.url.URL(
        drivername='postgresql+psycopg2',
        username=user,
        password=password,
        database=database,
        query={'host': host}
    )
    return str(url)


class Config():
    """ Base config class. """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """ Config for development environment. """
    pass

class TestConfig(Config):
    """ Config for test environment. """
    pass
