from . import Resource, request

from app.forms.authorization import AuthorizationForm

class AuthorizationResource(Resource):
    """ Authorization Resource class """

    def post(self):
        """ Authorize user via credentials """
        
        form = AuthorizationForm(params=request.get_json())
        if form.submit():
            return {'token': str(form.token)}, 200
        else:
            return {'errors': form.errors}, 400
