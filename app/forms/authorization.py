from .base import BaseForm, FormException

from app.models import db
from app.models.user import User
from app.services.authorization import encode_user
from app.utils.fields import EMAIL_REGEX
from app.utils.authorization import match_password


class AuthorizationForm(BaseForm):
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
        }
    }

    def submit(self):
        """ Perform authorization """

        if not self.is_valid():
            return False

        email = self.params.get('email')
        password = self.params.get('password')
        user = User.query.filter(User.email == email).first()
        if user and match_password(user, password):
            self.token = encode_user(user)
            return True
        else:
            self.errors['user'] = ['Invalid credentials']
            return False
