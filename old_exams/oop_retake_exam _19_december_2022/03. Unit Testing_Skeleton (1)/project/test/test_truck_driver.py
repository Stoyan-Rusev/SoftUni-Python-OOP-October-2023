from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver('Azis', 1.0)

    def test_init(self):
        self.assertEqual('Azis', self.driver.name)
        self.assertEqual(1.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual('Azis went bankrupt.', str(ve.exception))

    def test_add_cargo_offer_error(self):
        self.driver.available_cargos = {'KZ': 400}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('KZ', 400)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual({'KZ': 400}, self.driver.available_cargos)

    def test_add_cargo_offer_successfully(self):
        self.assertEqual({}, self.driver.available_cargos)
        result = self.driver.add_cargo_offer('KZ', 400)
        self.assertEqual("Cargo for 400 to KZ was added as an offer.", result)
        self.assertEqual({'KZ': 400}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_error(self):
        self.assertEqual({}, self.driver.available_cargos)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)
        self.assertEqual({}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_success(self):
        self.driver.available_cargos = {'KZ': 400, 'STZ': 1000}

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("Azis is driving 1000 to STZ.", result)
        self.assertEqual(875, self.driver.earned_money)
        self.assertEqual(1000, self.driver.miles)

    def test_drive_best_cargo_offer_success_long_distance_error(self):
        self.driver.available_cargos = {'KZ': 10000, 'STZ': 1000}

        with self.assertRaises(ValueError) as ve:
            result = self.driver.drive_best_cargo_offer()

        self.assertEqual('Azis went bankrupt.', str(ve.exception))
        # self.assertEqual(-1750, self.driver.earned_money)

    def test_drive_best_cargo_offer_success_long_distance(self):
        self.driver.money_per_mile = 2.0
        self.driver.available_cargos = {'KZ': 10000, 'STZ': 1000}

        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("Azis is driving 10000 to KZ.", result)
        self.assertEqual(8250, self.driver.earned_money)
        self.assertEqual(10000, self.driver.miles)

    def test_drive_best_cargo_offer_success_short_distance(self):
        self.driver.available_cargos = {'KZ': 200}

        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("Azis is driving 200 to KZ.", result)
        self.assertEqual(200, self.driver.earned_money)
        self.assertEqual(200, self.driver.miles)

    def test_repr(self):
        self.assertEqual("Azis has 0 miles behind his back.", repr(self.driver))


if __name__ == '__main__':
    main()
