from enum import Enum


class CabStatus(Enum):
    IDLE = "IDLE"
    ON_TRIP = "ON_TRIP"

    @staticmethod
    def get_status(status: str):
        for _status in CabStatus:
            if _status.value == status:
                return _status
        raise Exception("Status not exists")
