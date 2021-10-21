from application.cab import cab_repo


class TestCabRepo:

    def test_insert_initial_data(self):
        initial_data = [
            {
                "cab_id": 1,
                "cab_state": "IDLE",
                "city_id": 1
            }
        ]

        cab_repo.insert_initial_data(initial_data)
        assert len(cab_repo.vehicles) == len(initial_data)

    def test_register_cab(self):
        cab_data = {
            "cab_id": 2,
            "city_id": 1
        }

        actual_response = cab_repo.register_cab(cab_data)
        assert cab_repo.vehicles[2].get_json() == actual_response
