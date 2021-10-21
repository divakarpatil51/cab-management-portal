from unittest import mock
from application.cab.cab_service import insert_initial_data


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
