from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_correct_initialization(self):
        self.assertEqual('Tom', self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_when_cat_not_fed_expect_size_increase_and_sleepy(self):
        expected_size = self.cat.size + 1
        expected_sleepy_condition = True
        expected_fed_condition = True

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)
        self.assertEqual(expected_sleepy_condition, self.cat.sleepy)
        self.assertEqual(expected_fed_condition, self.cat.fed)

    def test_eat_when_cat_fed_expect_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_while_fed_expect_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertEqual(True, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)

    def test_sleep_while_cat_not_fed_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()

