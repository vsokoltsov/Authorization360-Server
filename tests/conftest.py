import os
import tempfile
from contextlib import contextmanager

import pytest
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import app
from app.models import db
from app.models.user import User
from app.utils.tests import CustomFlaskClient


@pytest.fixture(scope='session')
def flask_app():
    
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


@pytest.fixture(scope='function', autouse=True)
def db_session(monkeypatch):
    class Connection:
        def execute(self, *a, **kw):
            connection.execute(*a, **kw)

        def begin(self):
            return transaction_context()

    @contextmanager
    def db_engine_context():
        yield Connection()

    @contextmanager
    def transaction_context():
        yield transaction

    connection = db.engine.connect()
    transaction = connection.begin()
    session_factory = sessionmaker(bind=connection)
    db.session = session = scoped_session(session_factory)
    monkeypatch.setattr(db.engine, 'begin', db_engine_context)
    yield session
    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture
def user(db_session):
        user = User(email="example@mail.com", password="password")
        db_session.add(user)
        db_session.commit()
        return user