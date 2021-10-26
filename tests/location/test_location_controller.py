from unittest import mock


class TestLocationController:

    @mock.patch("application.location.location_controller.location_service.insert_location")
    def test_insert_location(self, insert_initial_data_mock, client):
        location = {
            "location_id": 5
        }
        expected_response = "Inserted location successfully"
        insert_initial_data_mock.return_value = expected_response
        actual_response = client.post("/rest/v1/location", json=location)
        assert actual_response.json == expected_response
        assert actual_response.status_code == 201

        insert_initial_data_mock.assert_called_once_with(location)
