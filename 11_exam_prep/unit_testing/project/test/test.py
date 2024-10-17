from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.group = Trip(10_000, 3, True)

    def test_init(self):
        self.assertEqual(10_000, self.group.budget)
        self.assertEqual(3, self.group.travelers)
        self.assertEqual(True, self.group.is_family)
        self.assertEqual({}, self.group.booked_destinations_paid_amounts)

    def test_class_attribute(self):
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500},
                         Trip.DESTINATION_PRICES_PER_PERSON)

    def test_traveller_setter_when_under_one(self):
        with self.assertRaises(ValueError) as ve:
            self.group.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_family_setter_when_group_under_2_people_and_true(self):
        self.group.travelers = 1
        self.group.is_family = True
        self.assertEqual(False, self.group.is_family)

    def test_family_setter_when_group_under_2_people_and_false(self):
        self.group.travelers = 1
        self.group.is_family = False
        self.assertEqual(False, self.group.is_family)

    def test_book_a_trip_when_trip_not_in_dict(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.group.book_a_trip('Kazanlak'))

    def test_book_a_trip_when_family_and_doesnt_have_budget(self):
        self.group.budget = 1000
        self.assertEqual('Your budget is not enough!', self.group.book_a_trip('Bulgaria'))

    def test_book_a_trip_when_not_family_and_doesnt_have_budget(self):
        self.group.budget = 1000
        self.group.is_family = False
        self.assertEqual('Your budget is not enough!', self.group.book_a_trip('Bulgaria'))

    def test_book_a_trip_when_family_and_have_budget(self):
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 8650.00',
                         self.group.book_a_trip('Bulgaria'))
        self.assertEqual({'Bulgaria': 1350},
                         self.group.booked_destinations_paid_amounts)

    def test_book_a_trip_when_not_family_and_have_budget(self):
        self.group.is_family = False
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 8500.00',
                         self.group.book_a_trip('Bulgaria'))
        self.assertEqual({'Bulgaria': 1500},
                         self.group.booked_destinations_paid_amounts)

    def test_booking_status_when_dict_empty(self):
        self.assertEqual(f'No bookings yet. Budget: 10000.00',
                         self.group.booking_status())

    def test_booking_status_when_dict_not_empty(self):
        self.group.budget = 7840
        self.group.booked_destinations_paid_amounts = {'Greece': 1500, 'Bulgaria': 900}
        self.assertEqual("Booked Destination: Bulgaria\nPaid Amount: 900.00\n"
                         "Booked Destination: Greece\nPaid Amount: 1500.00\n"
                         "Number of Travelers: 3\nBudget Left: 7840.00",
                         self.group.booking_status())


if __name__ == '__main__':
    main()
