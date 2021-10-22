import logging

from .vehicle import Vehicle
from .cab_status import CabStatus
from typing import Dict, List
from werkzeug.exceptions import BadRequest, NotFound

vehicles: Dict = {}

logger = logging.getLogger(__name__)


def insert_initial_data(cab_data):
    global vehicles

    vehicles = {vehicle['cab_id']: Vehicle(vehicle_id=vehicle['cab_id'], city_id=vehicle['city_id'],
                                           current_status=vehicle['cab_state']) for vehicle in cab_data}


def register_cab(cab_details):
    global vehicles
    cab_id = cab_details['cab_id']
    if cab_id in vehicles:
        raise BadRequest(description="Cab id already exists")

    vehicle = Vehicle(vehicle_id=cab_id, city_id=cab_details['city_id'],
                      current_status=CabStatus.IDLE.value,
                      registration_number=cab_details.get('registration_number', None))
    vehicles[cab_id] = vehicle
    return vehicle.get_json()


def update_location(cab_id, data):
    global vehicles

    if cab_id in vehicles:
        vehicles[cab_id].city_id = data['city_id']
        return vehicles[cab_id].get_json()
    else:
        raise NotFound("Cab with given cab id not found")


def update_cab_status(cab_id, data):
    global vehicles

    if cab_id not in vehicles:
        raise NotFound("Cab with given cab id not found")

    old_status = vehicles[cab_id].current_status
    vehicles[cab_id].current_status = data['current_status']
    if old_status != data['current_status'] and data['current_status'] == CabStatus.IDLE.value:
        vehicles[cab_id].update_trips_completed()
    return vehicles[cab_id].get_json()


def get_cabs() -> List[Vehicle]:
    global vehicles
    return [vehicle.get_json() for vehicle in vehicles.values()]
