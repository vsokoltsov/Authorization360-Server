from flask import Blueprint
from flask import jsonify
utils = Blueprint('utils', __name__)

@utils.route('/ping', methods=['GET'])
def ping():
    """ Show overall system state. """

    return jsonify({
        'message': 'Pong'
    })
