from . import cab_repo


def insert_initial_data(cab_data):
    cab_repo.insert_initial_data(cab_data=cab_data)
    return "Cab Data Inserted Successfully"
