from . import cab_repo
from .cab_status import CabStatus


def insert_initial_data(cab_data):
    cab_repo.insert_initial_data(cab_data=cab_data)
    return "Cab Data Inserted Successfully"


def register_cab(cab):
    return cab_repo.register_cab(cab)


def update_location(cab_id, data):
    return cab_repo.update_location(cab_id, data)


def update_cab_status(cab_id, data):
    return cab_repo.update_cab_status(cab_id, data)


def get_cabs():
    return cab_repo.get_cabs()


def book_cab(booking_details):
    available_cabs = cab_repo.get_cabs()
    if len(available_cabs) == 0:
        return "No cab available for booking at current location"

    curr_min = min(available_cabs, key=lambda cab: cab["trips_completed"])
    assigned_cab = next(filter(lambda cab: (cab["current_status"] == CabStatus.IDLE.value
                                            and cab["city_id"] == booking_details['current_city_id']
                                            and cab['trips_completed'] == curr_min["trips_completed"]),
                               available_cabs))
    assigned_cab = cab_repo.update_cab_status(assigned_cab["vehicle_id"], {"current_status": CabStatus.ON_TRIP.value})
    assigned_cab = cab_repo.update_location(assigned_cab["vehicle_id"], {"city_id": booking_details['next_city_id']})
    return assigned_cab
