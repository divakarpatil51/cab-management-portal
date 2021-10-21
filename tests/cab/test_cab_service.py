from unittest import mock
from application.cab.cab_service import insert_initial_data, register_cab


class TestCabService:

    @mock.patch("application.cab.cab_service.cab_repo.insert_initial_data")
    def test_insert_initial_data(self, insert_initial_data_mock):
        initial_data = [
            {
                "cab_id": 1,
                "cab_state": "IDLE",
                "city_id": 1
            }
        ]
        resp = insert_initial_data(initial_data)

        assert resp == "Cab Data Inserted Successfully"

        insert_initial_data_mock.assert_called_once_with(cab_data=initial_data)

    @mock.patch("application.cab.cab_service.cab_repo.register_cab")
    def test_register_cab(self, register_cab_mock):
        cab_data = {
            "cab_id": 1,
            "city_id": 1,
            "registration_number": 1,
        }
        expected_resp = {
            "cab_id": 1,
            "city_id": 1,
            "current_status": "IDLE",
            "registration_number": 1,
        }
        register_cab_mock.return_value = expected_resp
        actual_resp = register_cab(cab_data)

        assert actual_resp == expected_resp
        register_cab_mock.assert_called_once_with(cab_data)