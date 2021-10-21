from . import cab_repo


def insert_initial_data(cab_data):
    cab_repo.insert_initial_data(cab_data=cab_data)
    return "Cab Data Inserted Successfully"


def register_cab(cab):
    return cab_repo.register_cab(cab)
