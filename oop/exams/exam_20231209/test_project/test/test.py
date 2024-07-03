from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway_station = RailwayStation("NewStation")

    def test_low_len_name(self):
        expected_result = "Name should be more than 3 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = 'new'

        self.assertEqual(expected_result, str(ve.exception))

    def test_correct_len_name(self):
        self.assertEqual("NewStation", self.railway_station.name)

    def test_new_arrival_on_board(self):
        self.railway_station.new_arrival_on_board("new train")

        self.assertEqual(deque(["new train"]), self.railway_station.arrival_trains)

    def test_is_has_other_train_arrived_first(self):
        self.railway_station.arrival_trains = deque(["other train"])
        expected_result = f"There are other trains to arrive before our train."

        self.assertEqual(expected_result, self.railway_station.train_has_arrived("our train"))

    def test_train_has_arrived_and_ready_for_depart(self):
        expected_result = f"our train is on the platform and will leave in 5 minutes."
        self.railway_station.arrival_trains = deque(["our train"])

        self.assertEqual(expected_result, self.railway_station.train_has_arrived("our train"))
        self.assertEqual(deque(["our train"]), self.railway_station.departure_trains)

    def test_train_has_left(self):
        self.railway_station.departure_trains = deque(["our train"])

        self.assertTrue(self.railway_station.train_has_left("our train"))


if __name__ == "__main__":
    main()
