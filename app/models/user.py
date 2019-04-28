from datetime import datetime

import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

from . import db

class User(db.Model):
    """ User representation in the system. """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


    @hybrid_property
    def password(self):
        """ Return user's password """

        return self._password

    @password.setter
    def password(self, password):
        """ Set user's salt and password values. """

        self._password = bcrypt.hashpw(password, bcrypt.gensalt())
