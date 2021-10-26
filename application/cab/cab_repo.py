import logging

from .vehicle import Vehicle
from .cab_status import CabStatus
from typing import Dict, List
from werkzeug.exceptions import BadRequest, NotFound
from application.location import location_repo

vehicles: Dict[str, Vehicle] = {}

logger = logging.getLogger(__name__)


def insert_initial_data(cab_data):
    global vehicles
    vehicles = {vehicle['cab_id']: Vehicle(vehicle_id=vehicle['cab_id'],
                                           location=location_repo.get_location_by_id(vehicle.get('location_id', None)),
                                           current_status=CabStatus.get_status(vehicle['cab_state'])) for vehicle in
                cab_data}


def register_cab(cab_details):
    global vehicles
    cab_id = cab_details['cab_id']
    if cab_id in vehicles:
        raise BadRequest(description="Cab id already exists")

    vehicle = Vehicle(vehicle_id=cab_id, location=location_repo.get_location_by_id(cab_details['location_id']),
                      current_status=CabStatus.IDLE,
                      registration_number=cab_details.get('registration_number', None))
    vehicles[cab_id] = vehicle
    return vehicle.get_json()


def update_location(cab_id, location):
    global vehicles

    if cab_id in vehicles:
        vehicles[cab_id].location = location_repo.get_location_by_id(location['location_id'])
        return vehicles[cab_id].get_json()
    else:
        raise NotFound("Cab with given cab id not found")


def update_cab_status(cab_id, data):
    global vehicles

    if cab_id not in vehicles:
        raise NotFound("Cab with given cab id not found")

    old_status = vehicles[cab_id].current_status
    current_status = CabStatus.get_status(data['current_status'])
    vehicles[cab_id].current_status = current_status
    if old_status != current_status and data['current_status'] == CabStatus.IDLE.value:
        vehicles[cab_id].trip_completed()
    return vehicles[cab_id].get_json()


def get_cabs() -> List[Vehicle]:
    global vehicles
    return [vehicle.get_json() for vehicle in vehicles.values()]


def get_cabs_by_location(location_id: str) -> List[Vehicle]:
    global vehicles
    return [vehicle for vehicle in vehicles.values() if
            vehicle.location and vehicle.location.location_id == location_id]


def update_cab_trip(vehicle_id: str, assigned_cab: Vehicle):
    global vehicles
    vehicles[vehicle_id] = assigned_cab
    return vehicles[vehicle_id].get_json()


def get_cab_by_id(cab_id):
    global vehicles
    if cab_id not in vehicles:
        raise NotFound("Cab id not found")
    return vehicles[cab_id]
