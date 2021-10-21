from unittest import mock


class TestCabController:

    @mock.patch("application.cab.cab_controller.cab_service.insert_initial_data")
    def test_insert_initial_data(self, insert_initial_data_mock, client):
        initial_data = [
            {
                "cab_id": 1,
                "cab_state": "IDLE",
                "city_id": 1
            }
        ]
        expected_response = "Cab Data Inserted Successfully"
        insert_initial_data_mock.return_value = expected_response
        actual_response = client.post("/rest/v1/cab/insert-bulk", json=initial_data)
        assert actual_response.json == expected_response
        assert actual_response.status_code == 201

        insert_initial_data_mock.assert_called_once_with(initial_data)
