import logging

from .vehicle import Vehicle

vehicles: list = []

logger = logging.getLogger(__name__)


def insert_initial_data(cab_data):
    global vehicles
    vehicles = [Vehicle(vehicle_id=vehicle['cab_id'], location=vehicle['city_id'],
                        current_status=vehicle['cab_state'])
                for vehicle in cab_data]
