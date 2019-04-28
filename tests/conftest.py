import os
import tempfile

import pytest

import app
from app.models import db
from app.utils.tests import CustomFlaskClient


@pytest.fixture(scope='session')
def flask_app():
    
    os.environ['FLASK_ENV'] = 'test'
    os.environ['POSTGRES_DB'] = 'authorization360_testing'
    client = app.create_app()
    context = client.app_context()
    context.push()
    client.test_client_class = CustomFlaskClient
    yield client
    context.pop()


@pytest.fixture(scope='function')
def client(flask_app):
    with flask_app.test_client() as client:
        yield client
