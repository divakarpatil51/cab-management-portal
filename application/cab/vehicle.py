import dataclasses
import time
from typing import List

from application.cab.cab_status import CabStatus
from application.cab.trip import Trip
from application.location.location import Location


@dataclasses.dataclass
class Vehicle:
    vehicle_id: str
    location: Location
    current_status: CabStatus
    trips: List[Trip] = dataclasses.field(default_factory=list)
    registration_number: str = None

    def create_new_trip(self):
        trip = Trip(start_time=time.time())
        self.trips.append(trip)

    def get_json(self):
        return {
            "vehicle_id": self.vehicle_id,
            "location": self.location.location_id if self.location else None,
            "current_status": self.current_status.value,
        }
