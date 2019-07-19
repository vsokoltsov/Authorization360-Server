import pytest
import ujson

from app.services.authorization import AUTH_HEADER
from app.services.authorization import encode_user

def test_success_current_user_request(client, user):
    """ Test success user profile receiving with present token. """

    token = encode_user(user)
    headers = { AUTH_HEADER: token }
    response = client.get(
        '/api/v1/users/current', content_type="application/json",
        headers=headers
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 200
    assert 'current_user' in json_data

def test_failed_current_user_request(client, user):
    """ Test failed user profile request with empty token. """

    response = client.get(
        '/api/v1/users/current', content_type="application/json",
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 401
    assert 'error' in json_data
