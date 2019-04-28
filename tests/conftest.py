import os
import tempfile

import pytest

import app
from app.utils.tests import CustomFlaskClient


@pytest.fixture(scope='session')
def flask_app():
    client = app.create_app()
    context = client.app_context()
    context.push()
    client.test_client_class = CustomFlaskClient
    yield client
    context.pop()
