from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot('ID123', 'Military', 4, 10000.0)

    def test_init(self):
        self.assertEqual('ID123', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(4, self.robot.available_capacity)
        self.assertEqual(10000.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter_wrong_type(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Cooking'
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_price_setter_wrong_type(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_when_robot_have_current_component(self):
        self.robot.hardware_upgrades = ['rocket']
        self.assertEqual(['rocket'], self.robot.hardware_upgrades)
        result = self.robot.upgrade('rocket', 1000)
        self.assertEqual("Robot ID123 was not upgraded.", result)
        self.assertEqual(['rocket'], self.robot.hardware_upgrades)

    def test_upgrade_when_robot_doesnt_have_current_component(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual(10000, self.robot.price)

        result = self.robot.upgrade('rocket', 1000)

        self.assertEqual('Robot ID123 was upgraded with rocket.', result)
        self.assertEqual(['rocket'], self.robot.hardware_upgrades)
        self.assertEqual(11500, self.robot.price)

    def test_update_unsuccessful_due_to_version(self):
        self.robot.software_updates = [2.0, 1.9]

        result = self.robot.update(1.9, 4)

        self.assertEqual("Robot ID123 was not updated.", result)
        self.assertEqual([2.0, 1.9], self.robot.software_updates)

    def test_update_unsuccessful_due_to_capacity(self):
        self.robot.software_updates = [2.0, 1.9]

        result = self.robot.update(2.1, 5)

        self.assertEqual("Robot ID123 was not updated.", result)
        self.assertEqual([2.0, 1.9], self.robot.software_updates)

    def test_update_successful_when_has_updates_already(self):
        self.robot.software_updates = [2.0, 1.9]
        self.assertEqual([2.0, 1.9], self.robot.software_updates)
        self.assertEqual(4, self.robot.available_capacity)

        result = self.robot.update(2.1, 4)

        self.assertEqual('Robot ID123 was updated to version 2.1.', result)
        self.assertEqual([2.0, 1.9, 2.1], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)

    def test_update_successful_when_first_update(self):
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(4, self.robot.available_capacity)

        result = self.robot.update(2.1, 4)

        self.assertEqual('Robot ID123 was updated to version 2.1.', result)
        self.assertEqual([2.1], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)

    def test_gt(self):
        test_robot = Robot('TEST ID', 'Military', 5, 10000)
        result = self.robot > test_robot
        self.assertEqual('Robot with ID ID123 costs equal to Robot with ID TEST ID.', result)

        test_robot = Robot('TEST ID', 'Military', 5, 9999)
        result = self.robot > test_robot
        self.assertEqual('Robot with ID ID123 is more expensive than Robot with ID TEST ID.', result)

        test_robot = Robot('TEST ID', 'Military', 5, 10001)
        result = self.robot > test_robot
        self.assertEqual('Robot with ID ID123 is cheaper than Robot with ID TEST ID.', result)


if __name__ == '__main__':
    main()
