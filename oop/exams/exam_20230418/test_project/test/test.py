from unittest import TestCase, main

from test_project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot('R01', 'Military', 5, 100)


    def test_correct_init(self):
        self.assertEqual('R01', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_miss_category_raise_valueerror(self):
        expected = f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'"

        with self.assertRaises(ValueError) as ve:
            self.no_category = Robot('R01', 'miss', 5, 100)

        self.assertEqual(expected, str(ve.exception))

    def test_negative_price_raise_valueerror(self):
        expected = "Price cannot be negative!"

        with self.assertRaises(ValueError) as ve:
            self.negative_price = Robot('R01', 'Military', 5, -1)

        self.assertEqual(expected, str(ve.exception))

    def test_upgrade_with_already_added_hardware(self):
        expected = f"Robot {self.robot.robot_id} was not upgraded."
        self.robot.upgrade('head', 20)

        self.assertEqual(expected, self.robot.upgrade('head', 20))

    def test_upgrade_add_hardware_with_sucses(self):
        expected = f'Robot {self.robot.robot_id} was upgraded with head.'
        self.assertEqual(expected, self.robot.upgrade('head', 20))

        self.assertEqual(['head'], self.robot.hardware_upgrades)
        self.assertEqual(100+20*self.robot.PRICE_INCREMENT, self.robot.price)

    def test_software_not_updated_with_low_version(self):
        self.robot.update(2,2)
        expected = f"Robot {self.robot.robot_id} was not updated."

        self.assertEqual(expected, self.robot.update(1, 2))

    def test_software_not_updated_low_capacity(self):
        self.robot.update(2,2)
        expected = f"Robot {self.robot.robot_id} was not updated."

        self.assertEqual(expected, self.robot.update(4, 4))

    def test_software_updated_succssessfuly(self):
        self.robot.update(2,2)
        expected = f"Robot {self.robot.robot_id} was updated to version 3."

        self.assertEqual(expected, self.robot.update(3, 3))

    def test_gt_our_is_expensive(self):
        self.other = Robot('O01', 'Military', 4, 50)
        expected = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.other.robot_id}.'

        result = self.robot > self.other
        self.assertEqual(expected, result)

    def test_gt_other_is_expensive(self):
        self.other = Robot('O01', 'Military', 4, 200)
        expected = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.other.robot_id}.'

        result = self.robot > self.other
        self.assertEqual(expected, result)

    def test_gt_same_price(self):
        self.other = Robot('O01', 'Military', 4, 100)
        expected = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.other.robot_id}.'

        result = self.robot > self.other
        self.assertEqual(expected, result)


if __name__ == '__mian__':
    main()
