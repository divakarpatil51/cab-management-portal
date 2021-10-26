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


@cab_blueprint.route("/<int:cab_id>/update-location", methods=['PATCH'])
def update_location(cab_id):
    response = cab_service.update_location(cab_id, request.json)
    return jsonify(response), 200


@cab_blueprint.route("/<int:cab_id>/update-status", methods=['PATCH'])
def update_cab_status(cab_id):
    response = cab_service.update_cab_status(cab_id, request.json)
    return jsonify(response), 200


@cab_blueprint.route("/book-cab", methods=['POST'])
def book_cab():
    booking_status = cab_service.book_cab(request.json)
    return jsonify(booking_status), 200


@cab_blueprint.route("", methods=['GET'])
def get_cabs():
    return jsonify(cab_service.get_cabs())


@cab_blueprint.route("/<int:cab_id>/history", methods=["GET"])
def cab_history(cab_id):
    return jsonify(cab_service.get_cab_history(cab_id))
