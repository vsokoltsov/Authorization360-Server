import pytest
import ujson

from app.models.user import User

def test_success_registration(client):
    """Test success user registration."""

    data = {
        'email': 'example@mail.com',
        'password': 'password',
        'password_confirmation': 'password'
    }
    response = client.post(
        '/api/v1/sign_up', data=ujson.dumps(data), content_type="application/json"
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 201
    assert 'token' in json_data

def test_registration_user_creation(client):
    """ Test success creation of the user. """

    users_count = User.query.count()
    data = {
        'email': 'example@mail.com',
        'password': 'password',
        'password_confirmation': 'password'
    }
    response = client.post(
        '/api/v1/sign_up', data=ujson.dumps(data), content_type="application/json"
    )
    assert User.query.count() == users_count + 1

def test_failed_registration(client):
    """ Test failed user registration. """

    data = {}
    response = client.post(
        '/api/v1/sign_up', data=ujson.dumps(data), content_type="application/json"
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 400
    assert 'errors' in json_data
