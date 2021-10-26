import dataclasses
import time
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
    current_status: TripStatusEnum = TripStatusEnum.STARTED

    def update_status(self, status: TripStatusEnum):
        if status == TripStatusEnum.COMPLETED:
            self.end_time = time.time()
        trip_status = TripStatus(status=status)
        self.status_changes.append(trip_status)

    def to_json(self):
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "current_status": self.current_status.value,
        }
