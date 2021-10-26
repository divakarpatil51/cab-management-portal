from application.cab import cab_repo
from unittest import mock


class TestCabRepo:

    @mock.patch("application.cab.cab_repo.location_repo.get_location_by_id")
    def test_insert_initial_data(self, location_mock):
        initial_data = [
            {
                "cab_id": '1',
                "cab_state": "IDLE",
                "location_id": '1'
            }
        ]

        cab_repo.insert_initial_data(initial_data)
        assert len(cab_repo.vehicles) == len(initial_data)

    @mock.patch("application.cab.cab_repo.location_repo.get_location_by_id")
    def test_register_cab(self, location_mock):
        cab_data = {
            "cab_id": '2',
            "location_id": 1
        }

        actual_response = cab_repo.register_cab(cab_data)
        assert cab_repo.vehicles['2'].get_json() == actual_response
