from typing import Dict, List, Union

from werkzeug.exceptions import BadRequest, NotFound

from . import cab_repo
from .cab_status import CabStatus
from ..location import location_service


def insert_initial_data(cab_data: List[Dict]) -> str:
    location_data = [{"location_id": data.get('location_id', None)} for data in cab_data]
    location_service.insert_locations_in_batch(location_data=location_data)

    cab_repo.insert_initial_data(cab_data=cab_data)

    return "Cab Data Inserted Successfully"


def register_cab(cab: Dict) -> Dict:
    return cab_repo.register_cab(cab)


def update_location(cab_id: str, location: Dict) -> Dict:
    if not location_service.does_location_exist(location_id=location['location_id']):
        raise BadRequest("Cab service not available at given location")
    return cab_repo.update_location(cab_id, location)


def update_cab_status(cab_id: str, data: Dict) -> Dict:
    return cab_repo.update_cab_status(cab_id, data)


def get_cabs() -> List:
    return cab_repo.get_cabs()


def book_cab(booking_details: Dict) -> Union[str, Dict]:

    if not location_service.does_location_exist(booking_details['next_location_id']):
        raise NotFound("Cab service not available at given location")
    print(
        cab_repo.get_cabs_by_location(booking_details['current_location_id']))
    available_cabs = list(filter(lambda vehicle: vehicle.current_status == CabStatus.IDLE,
                                 cab_repo.get_cabs_by_location(booking_details['current_location_id'])))

    if len(available_cabs) == 0:
        raise NotFound("No cab available for booking at current location")

    assigned_cab = min(available_cabs, key=lambda cab: len(cab.trips))
    assigned_cab.create_new_trip()
    assigned_cab.current_status = CabStatus.ON_TRIP
    assigned_cab.location = location_service.get_location_by_id(location_id=booking_details['next_location_id'])
    assigned_cab = cab_repo.update_cab_trip(assigned_cab.vehicle_id, assigned_cab)
    return assigned_cab


def get_cab_history(cab_id):
    cab = cab_repo.get_cab_by_id(cab_id)
    return cab.get_json()