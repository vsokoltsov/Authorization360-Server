import pytest
import ujson


def test_success_authorization(client, user):
    """ Test success authorization request. """

    data = {
        'email': user.email,
        'password': 'password'
    }
    response = client.post(
        '/api/v1/sign_in', data=ujson.dumps(data), content_type="application/json"
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 200
    assert 'token' in json_data

def test_failed_authorization(client, user):
    """ Test failed authorization request. """

    response = client.post(
        '/api/v1/sign_in', data=ujson.dumps({}), content_type="application/json"
    )
    json_data = ujson.loads(response.data)
    assert response.status_code == 400
    assert 'errors' in json_data
