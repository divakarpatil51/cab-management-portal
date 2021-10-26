from application.location import location_repo
from typing import Dict, List
from werkzeug.exceptions import BadRequest

from application.location.location import Location


def insert_location(location_data: Dict) -> str:
    if location_repo.does_location_exist(location_id=location_data['location_id']):
        raise BadRequest("Location already exists")
    location_repo.insert_location(location_data=location_data)
    return "Inserted location successfully"


def insert_locations_in_batch(location_data: List[Dict]) -> str:
    location_repo.insert_locations_in_batch(location_data=location_data)
    return f"Inserted {len(location_data)} locations successfully"


def does_location_exist(location_id: str) -> bool:
    return location_repo.does_location_exist(location_id)


def get_location_by_id(location_id: str) -> Location:
    return location_repo.get_location_by_id(location_id=location_id)
