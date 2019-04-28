import ujson
from flask import url_for
from flask.testing import FlaskClient

class CustomFlaskClient(FlaskClient):
    def login(self, user):
        with self.session_transaction() as session:
            session['user'] = {'id': user.id}

    def json_request(self, url, data, method):
        return self.open(
            url, data=ujson.dumps(data), content_type='application/json', method=method
        )

    def post_json(self, url, data):
        return self.json_request(url, data, method='POST')

    def put_json(self, url, data):
        return self.json_request(url, data, method='PUT')
