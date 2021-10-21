from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, NotFound

exec_blueprint = Blueprint("exec_blueprint", __name__)


@exec_blueprint.app_errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(e.description), 400


@exec_blueprint.app_errorhandler(NotFound)
def handle_not_found(e):
    return jsonify(e.description), 404
