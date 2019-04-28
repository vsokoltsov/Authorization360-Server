""" Authorization utils. """

import bcrypt

def match_password(user, password):
    """ 
    Match user hashed password and the given value.
    
    :param user: User instance
    :param password: Human readable password value
    :return: Whether or not password matches
    :rtype: boolean
    """

    return user.password == bcrypt.hashpw(password, user.password)
