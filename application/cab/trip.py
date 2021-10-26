import dataclasses
from enum import Enum
from typing import List


class TripStatusEnum(Enum):
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"


@dataclasses.dataclass
class TripStatus:
    status: TripStatusEnum


@dataclasses.dataclass
class Trip:

    start_time: float
    end_time: float = None
    status_changes: List[TripStatus] = dataclasses.field(default_factory=list)
    current_status: str = TripStatusEnum.STARTED

    def update_status(self, status: TripStatusEnum):
        trip_status = TripStatus(status=status)
        self.status_changes.append(trip_status)
