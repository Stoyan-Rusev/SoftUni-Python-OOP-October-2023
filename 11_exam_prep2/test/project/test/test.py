from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar('M5', 'Sedan', 100_000, 20_000.0)
        self.car2 = SecondHandCar('M5', 'Combi', 100_000, 20_000.0)

    def test_init(self):
        self.assertEqual('M5', self.car.model)
        self.assertEqual('Sedan', self.car.car_type)
        self.assertEqual(100_000, self.car.mileage)
        self.assertEqual(20_000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_correct(self):
        self.car.price = 30_000
        self.assertEqual(30000, self.car.price)

    def test_price_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1
        self.assertEqual('Price should be greater than 1.0!',
                         str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0
        self.assertEqual('Price should be greater than 1.0!',
                         str(ve.exception))

    def test_mileage_setter_correct(self):
        self.car.mileage = 40_000
        self.assertEqual(40000, self.car.mileage)

    def test_mileage_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ve.exception))

    def test_promotional_price_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(20_000.0)

        self.assertEqual('You are supposed to decrease the price!',
                         str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(21_000.0)

        self.assertEqual('You are supposed to decrease the price!',
                         str(ve.exception))

    def test_promotional_price_when_new_price_correct(self):
        self.assertEqual(20000.0, self.car.price)
        result = self.car.set_promotional_price(19_999.0)
        self.assertEqual(19_999.0, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_error(self):
        self.assertEqual([], self.car.repairs)
        self.assertEqual(20000, self.car.price)

        result = self.car.need_repair(11_000, 'gearbox failure')
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual([], self.car.repairs)
        self.assertEqual(20000, self.car.price)

    def test_need_repair_correct(self):
        self.assertEqual(20_000, self.car.price)
        self.assertEqual([], self.car.repairs)

        result = self.car.need_repair(3_000, 'timing chain replacement')

        self.assertEqual('Price has been increased due to repair charges.',
                         result)
        self.assertEqual(23_000.0, self.car.price)
        self.assertEqual(['timing chain replacement'], self.car.repairs)

    def test_need_repair_correct_second(self):
        self.assertEqual(20_000, self.car.price)
        self.assertEqual([], self.car.repairs)

        result = self.car.need_repair(10_000, 'timing chain replacement')

        self.assertEqual('Price has been increased due to repair charges.',
                         result)
        self.assertEqual(30_000.0, self.car.price)
        self.assertEqual(['timing chain replacement'], self.car.repairs)

    def test_gt_when_mismatch(self):
        result = self.car > self.car2
        self.assertEqual('Cars cannot be compared. Type mismatch!',
                         result)

    def test_gt_when_match(self):
        self.car2.car_type = 'Sedan'
        result = self.car > self.car2
        self.assertEqual(False, result)

    def test_str(self):
        self.assertEqual(f"""Model M5 | Type Sedan | Milage 100000km
Current price: 20000.00 | Number of Repairs: 0""", self.car.__str__())


if __name__ == '__main__':
    main()
