from flask import Blueprint, jsonify, request
from . import location_service

location_blueprint = Blueprint("location_blueprint", __name__, url_prefix="/rest/v1/location")


@location_blueprint.route("", methods=["POST"])
def insert_location():
    response = location_service.insert_location(request.json)
    return jsonify(response), 201
