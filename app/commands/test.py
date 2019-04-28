import sys

from flask.cli import with_appcontext
import click
import pytest

from app.models import db

class create_test_db():
    def __init__(self):
        pass

    def __enter__(self):
        db.drop_all()
        db.create_all()

    def __exit__(self, type, value, traceback):
        db.drop_all()


@click.command('test')
@click.argument('path', nargs=-1,)
@with_appcontext
def test(path):
    """ Run tests """

    result_code = 1
    with create_test_db():
        result_code = pytest.main(sys.argv[2:])
    sys.exit(result_code)
