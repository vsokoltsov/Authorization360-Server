import pytest

from app.models.user import User
from app.forms.registration import RegistrationForm

def test_success_form_validation():
    """ Test success form validation. """

    data = {
        'email': 'example@mail.com',
        'password': 'password',
        'password_confirmation': 'password'
    }
    form = RegistrationForm(params=data)
    assert form.is_valid() == True

def test_failed_form_validation():
    """ Test failed form validation. """

    data = {}
    form = RegistrationForm(params=data)
    assert form.is_valid() == False

def test_success_user_creation():
    """ Test success user creation. """

    users_count = User.query.count()
    data = {
        'email': 'example@mail.com',
        'password': 'password',
        'password_confirmation': 'password'
    }
    form = RegistrationForm(params=data)
    form.submit()
    assert User.query.count() == users_count + 1

def test_failed_form_submit_user_exist(user):
    """ Test failed form submit if user with this email already exist. """

    data = {
        'email': user.email,
        'password': 'password',
        'password_confirmation': 'password'
    }
    form = RegistrationForm(params=data)
    assert form.submit() == False
