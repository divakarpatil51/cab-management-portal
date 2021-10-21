
class Vehicle:

    def __init__(self, vehicle_id, location, current_status, registration_number=None):
        self.vehicle_id = vehicle_id
        self.location = location
        self.current_status = current_status
        self.registration_number = registration_number

    def get_json(self):
        return vars(self)