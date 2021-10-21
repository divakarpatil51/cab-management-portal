from . import cab_repo


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
