from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation('Sofia')

    def test_init(self):
        self.assertEqual('Sofia', self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_setter_correct(self):
        self.new_station = RailwayStation('Sofi')
        self.assertEqual('Sofi', self.new_station.name)

    def test_name_setter_error_len_equals_three(self):
        with self.assertRaises(ValueError) as ve:
            self.new_station = RailwayStation('Sof')
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_error_len_smaller_than_three(self):
        with self.assertRaises(ValueError) as ve:
            self.new_station = RailwayStation('So')
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.station.new_arrival_on_board('Sofia - Plovdiv')
        self.assertEqual(deque(['Sofia - Plovdiv']), self.station.arrival_trains)

    def test_train_has_arrived_unsuccessfully_due_to_have_trains_in_deque_and_incorrect_train(self):
        self.station.arrival_trains = deque(['Sofia - Plovdiv', 'Vraca - Kazanlak'])
        self.station.departure_trains = deque([])

        result = self.station.train_has_arrived('Vraca - Kazanlak')

        self.assertEqual("There are other trains to arrive before Vraca - Kazanlak.", result)
        self.assertEqual(deque(['Sofia - Plovdiv', 'Vraca - Kazanlak']), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_arrived_successfully(self):
        self.station.arrival_trains = deque(['Sofia - Plovdiv', 'Vraca - Kazanlak'])
        self.station.departure_trains = deque([])

        result = self.station.train_has_arrived('Sofia - Plovdiv')

        self.assertEqual("Sofia - Plovdiv is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['Vraca - Kazanlak']), self.station.arrival_trains)
        self.assertEqual(deque(['Sofia - Plovdiv']), self.station.departure_trains)

    def test_train_has_left_successfully(self):
        self.station.departure_trains = deque(['Sofia - Plovdiv', 'Vraca - Kazanlak'])

        result = self.station.train_has_left('Sofia - Plovdiv')

        self.assertEqual(deque(['Vraca - Kazanlak']), self.station.departure_trains)
        self.assertEqual(True, result)

    def test_train_has_left_unsuccessfully(self):
        self.station.departure_trains = deque(['Sofia - Plovdiv', 'Vraca - Kazanlak'])

        result = self.station.train_has_left('Vraca - Kazanlak')

        self.assertEqual(deque(['Sofia - Plovdiv', 'Vraca - Kazanlak']), self.station.departure_trains)
        self.assertEqual(False, result)


if __name__ == '__main__':
    main()
