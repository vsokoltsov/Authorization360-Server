import sqlalchemy

from .base import BaseForm
from app.models import db
from app.models.user import User
from app.services.authorization import encode_user
from app.utils.fields import EMAIL_REGEX

class RegistrationForm(BaseForm):
    schema = {
        'email': {
            'type': 'string',
            'empty': False,
            'required': True,
            'regex': EMAIL_REGEX,
        },
        'password': {
            'type': 'string',
            'empty': False,
            'required': True
        },
        'password_confirmation': {
            'type': 'string',
            'empty': False,
            'required': True,
            'equal': 'password',
        }
    }

    def submit(self):
        """ Perform registration """

        if not self.is_valid():
            return False

        try:
            email = self.params.get('email')
            password = self.params.get('password')
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            self.token = encode_user(user)
            return True
        except sqlalchemy.exc.IntegrityError:
            self.errors['user'] = ['User with this email already exists']
            return False
