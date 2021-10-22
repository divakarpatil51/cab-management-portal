class Vehicle:

    def __init__(self, vehicle_id, city_id, current_status, registration_number=None):
        self.vehicle_id = vehicle_id
        self.city_id = city_id
        self.current_status = current_status
        self.registration_number = registration_number
        self.trips_completed = 0

    def update_trips_completed(self):
        self.trips_completed += 1

    def get_json(self):
        return vars(self)
