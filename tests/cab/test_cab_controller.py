from unittest import mock


class TestCabController:

    @mock.patch("application.cab.cab_controller.cab_service.insert_initial_data")
    def test_insert_initial_data(self, insert_initial_data_mock, client):
        initial_data = [
            {
                "cab_id": '1',
                "cab_state": "IDLE",
                "location_id": '1'
            }
        ]
        expected_response = "Cab Data Inserted Successfully"
        insert_initial_data_mock.return_value = expected_response
        actual_response = client.post("/rest/v1/cab/insert-bulk", json=initial_data)
        assert actual_response.json == expected_response
        assert actual_response.status_code == 201

        insert_initial_data_mock.assert_called_once_with(initial_data)

    @mock.patch("application.cab.cab_controller.cab_service.register_cab")
    def test_register_cab(self, register_cab_mock, client):
        cab_data = {
            "cab_id": '1',
            "location_id": '1',
            "registration_number": '1'
        }
        expected_response = {
            "current_status": "IDLE",
            "location_id": '1',
            "registration_number": '1',
            "vehicle_id": '1'
        }
        register_cab_mock.return_value = expected_response
        actual_response = client.post("/rest/v1/cab", json=cab_data)
        assert actual_response.json == expected_response
        assert actual_response.status_code == 201

        register_cab_mock.assert_called_once_with(cab_data)

    @mock.patch("application.cab.cab_controller.cab_service.update_location")
    def test_update_location(self, update_location_mock, client):
        location = {
            "location_id": 1
        }
        expected_output = {
            "current_status": "IDLE",
            "location": 1,
            "vehicle_id": 2
        }
        update_location_mock.return_value = expected_output
        actual_response = client.patch("/rest/v1/cab/1/update-location", json=location)
        assert actual_response.json == expected_output
        assert actual_response.status_code == 200

    @mock.patch("application.cab.cab_controller.cab_service.update_cab_status")
    def test_update_cab_status(self, update_cab_status_mock, client):
        status = {
            "current_status": "IDLE"
        }
        expected_output = {
            "current_status": "IDLE",
            "location": 2,
            "trips": [
                {
                    "current_status": "STARTED",
                    "end_time": 1635235587.21774,
                    "start_time": 1635235584.43007
                }
            ],
            "vehicle_id": 3
        }
        update_cab_status_mock.return_value = expected_output
        actual_response = client.patch("/rest/v1/cab/1/update-status", json=status)
        assert actual_response.json == expected_output
        assert actual_response.status_code == 200

    @mock.patch("application.cab.cab_controller.cab_service.book_cab")
    def book_cab(self, client, book_cab_mock):
        status = {
            "current_location_id": 1,
            "next_location_id": 2
        }
        expected_output = {
            "current_status": "ON_TRIP",
            "location": 2,
            "trips": [
                {
                    "current_status": "STARTED",
                    "end_time": None,
                    "start_time": 1635235584.43007
                }
            ],
            "vehicle_id": 3
        }
        book_cab_mock.return_value = expected_output
        actual_response = client.post("/rest/v1/cab/book-cab", json=status)
        assert actual_response == expected_output

    @mock.patch("application.cab.cab_controller.cab_service.get_cabs")
    def get_cabs(self, client, get_cabs_mock):

        expected_output = [
            {
                "current_status": "ON_TRIP",
                "location": None,
                "trips": [],
                "vehicle_id": 1
            },
            {
                "current_status": "IDLE",
                "location": 2,
                "trips": [],
                "vehicle_id": 2
            },
            {
                "current_status": "IDLE",
                "location": 1,
                "trips": [],
                "vehicle_id": 3
            }
        ]
        get_cabs_mock.return_value = expected_output
        actual_response = client.get("/rest/v1/cab")
        assert actual_response == expected_output

    @mock.patch("application.cab.cab_controller.cab_service.cab_history")
    def cab_history(self, client, cab_history):
        expected_output = [
            {
                "current_status": "ON_TRIP",
                "location": None,
                "trips": [],
                "vehicle_id": 1
            },
            {
                "current_status": "IDLE",
                "location": 2,
                "trips": [],
                "vehicle_id": 2
            },
            {
                "current_status": "IDLE",
                "location": 1,
                "trips": [],
                "vehicle_id": 3
            }
        ]
        cab_history.return_value = expected_output
        actual_response = client.get("/rest/v1/cab/1/history")
        assert actual_response == expected_output
