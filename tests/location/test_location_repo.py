from unittest import mock

from application.location import location_repo


class TestLocationRepo:

    @mock.patch("application.location.location_repo.locations")
    @mock.patch("application.location.location_repo.Location")
    def test_insert_location(self, location_mock, locations_mock):
        location = {
            "location_id": "1"
        }
        locations_mock.return_value = [location]
        location_mock.return_value = location
        location_repo.insert_location(location)
        locations_mock.append.assert_called_once_with(location)

    @mock.patch("application.location.location_repo.locations")
    @mock.patch("application.location.location_repo.Location")
    def test_insert_locations_in_batch(self, location_mock, locations_mock):
        location = [{
            "location_id": "1"
        }]
        locations_mock.return_value = location
        location_mock.return_value = location
        location_repo.insert_locations_in_batch(location)
        locations_mock.append.assert_called_once_with(location)

