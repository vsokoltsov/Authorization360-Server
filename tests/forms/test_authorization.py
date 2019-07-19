import pytest

from app.models.user import User
from app.forms.authorization import AuthorizationForm


def test_success_validation(user):
    """ Test success form validation. """

    data = {
        'email': user.email,
        'password': 'password',
    }
    form = AuthorizationForm(params=data)
    assert form.is_valid() == True

def test_failed_validation():
    """ Test failed validation. """

    form = AuthorizationForm(params={})
    assert form.is_valid() == False

def test_success_submit(user):
    """ Test success submit. """

    data = {
        'email': user.email,
        'password': 'password',
    }
    form = AuthorizationForm(params=data)
    assert form.submit() == True

def test_failed_submit():
    """ Test failed submit. """

    form = AuthorizationForm(params={})
    assert form.submit() == False

def test_success_token_generation(user):
    """ Test success token generation if form is submitted. """

    data = {
        'email': user.email,
        'password': 'password',
    }
    form = AuthorizationForm(params=data)
    form.submit()
    assert form.token is not None

def test_failed_submit_wrong_password(user):
    """ Test failed validation is password does not match. """

    data = {
        'email': user.email,
        'password': 'pas',
    }
    form = AuthorizationForm(params=data)
    form.submit()
    assert form.errors['user'] is not None


