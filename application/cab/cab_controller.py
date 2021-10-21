from flask import Blueprint, jsonify, request
from . import cab_service


cab_blueprint = Blueprint("cab_blueprint", __name__, url_prefix="/rest/v1/cab")


@cab_blueprint.route("/insert-bulk", methods=['POST'])
def insert_initial_data():
    response = cab_service.insert_initial_data(request.json)
    return jsonify(response), 201


@cab_blueprint.route("", methods=["POST"])
def register_cab():
    response = cab_service.register_cab(request.json)
    return jsonify(response), 201
