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
