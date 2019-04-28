import sys
import os

from flask.cli import with_appcontext
import click
import pytest
from alembic.config import Config
from alembic import command
from pathlib import Path
import alembic
from app.config import get_database_path

from app.models import db

class create_test_db():
    def __init__(self):
        pass

    def __enter__(self):
        alembic_conf_path = os.path.join(
            Path(__file__).parent.parent.parent, 'alembic', 'alembic.ini'
        )
        alembic_cfg = Config(alembic_conf_path)
        db.drop_all()
        alembic_cfg.set_main_option('sqlalchemy.url', get_database_path())
        command.upgrade(alembic_cfg, "head")

    def __exit__(self, type, value, traceback):
        db.drop_all()


@click.command('test')
@click.argument('path', nargs=-1,)
@with_appcontext
def test(path):
    """ Run tests """

    result_code = 1
    with create_test_db():
        result_code = pytest.main(['-s'] + sys.argv[2:])
    sys.exit(result_code)
