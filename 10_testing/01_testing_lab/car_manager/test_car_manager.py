from unittest import TestCase, main
from car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car('BMW', 'M5',
                       20, 80)

    def test_init(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual('M5', self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_emtpy_make_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_emtpy_model_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be "
                         "zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be "
                         "zero or negative!", str(ex.exception))

    def test_zero_fuel_amount_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_amount_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!",
                         str(ex.exception))

    def test_refueling_when_not_enough_space(self):
        expected_tank_amount = self.car.fuel_capacity

        self.car.refuel(1000)

        self.assertEqual(expected_tank_amount, self.car.fuel_amount)

    def test_drive_when_enough_fuel_expect_fuel_amount_decreased(self):
        self.car.fuel_amount = 40
        expected_amount_after_driving = 20

        self.car.drive(100)

        self.assertEqual(expected_amount_after_driving, self.car.fuel_amount)

    def test_drive_when_not_enough_fuel(self):
        self.car.fuel_amount = 19

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!",
                         str(ex.exception))


if __name__ == '__main__':
    main()
