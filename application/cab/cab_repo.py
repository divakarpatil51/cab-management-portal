import logging

from .vehicle import Vehicle
from .cab_status import CabStatus

vehicles: list = []

logger = logging.getLogger(__name__)


def insert_initial_data(cab_data):
    global vehicles
    vehicles = [Vehicle(vehicle_id=vehicle['cab_id'], city_id=vehicle['city_id'],
                        current_status=vehicle['cab_state'])
                for vehicle in cab_data]


def register_cab(cab_details):
    global vehicles
    vehicle = Vehicle(vehicle_id=cab_details['cab_id'], city_id=cab_details['city_id'],
                      current_status=CabStatus.IDLE.value,
                      registration_number=cab_details.get('registration_number', None))
    return vehicle.get_json()