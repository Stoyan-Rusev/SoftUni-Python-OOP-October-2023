from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(2.5, 200.0)

    def test_init(self):
        self.assertEqual(2.5, self.car.fuel)
        self.assertEqual(2.5, self.car.capacity)
        self.assertEqual(200, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_init_types(self):
        self.assertIsInstance(self.car.fuel, float)
        self.assertIsInstance(self.car.capacity, float)
        self.assertIsInstance(self.car.horse_power, float)
        self.assertIsInstance(self.car.fuel_consumption, float)

    def test_drive_when_car_have_enough_fuel(self):
        self.car.drive(2)

        self.assertEqual(0, self.car.fuel)

    def test_drive_when_car_doesnt_have_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(3)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_when_overfilling_tank(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_amount(self):
        self.car.fuel = 0
        self.car.refuel(2)

        self.assertEqual(2, self.car.fuel)

    def test_str(self):
        expected_str = (f"The vehicle has 200.0  horse power "
                        f"with 2.5 fuel left and 1.25 fuel consumption")

        self.assertEqual(expected_str, str(self.car))


if __name__ == '__main__':
    main()
