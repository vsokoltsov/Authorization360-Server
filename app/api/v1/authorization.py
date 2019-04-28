from . import Resource


class AuthorizationResource(Resource):
    """ Authorization Resource class """

    def post(self):
        """ Authorize user via credentials """
        return "Hello world"
