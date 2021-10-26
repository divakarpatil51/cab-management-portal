from typing import List, Dict
from .location import Location
from werkzeug.exceptions import NotFound

locations: List = []


def insert_location(location_data: Dict):
    global locations
    location = Location(location_id=location_data['location_id'])
    locations.append(location)


def insert_locations_in_batch(location_data: List[Dict]):
    global locations
    for location in location_data:
        _location = Location(location_id=location['location_id'])
        locations.append(_location)


def get_locations():
    global locations
    return locations


def get_location_by_id(location_id: str):
    global locations
    if location_id is None:
        return None
    return next(filter(lambda location: location.location_id == location_id, locations))


def does_location_exist(location_id: str):
    global locations
    print(len(list(filter(lambda location: location.location_id == location_id, locations))) > 0)
    return len(list(filter(lambda location: location.location_id == location_id, locations))) > 0
