import sys
import os

from flask.cli import with_appcontext
import click
import pytest
from app.config import get_database_path

from app.models import db
from app.utils.db import run_migrations

class create_test_db():
    def __init__(self):
        pass

    def __enter__(self):
        db.drop_all()
        run_migrations()

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
