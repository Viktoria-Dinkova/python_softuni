from unittest import TestCase, main
from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("new", 2)

    def test_correct_init(self):
        self.assertEqual('new', self.restaurant.name)
        self.assertEqual(2, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_no_name_raise_valerror(self):
        expected = "Invalid name!"

        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = None
            self.assertEqual(expected, str(ve.exception))

    def test_no_whitespaces_name_raise_valerror(self):
        expected = "Invalid name!"

        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = '    '
            self.assertEqual(expected, str(ve.exception))

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1
            self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_if_have_proper(self):
        self.restaurant.waiters = [{'name': 'w1', 'total_earnings': 70}, {'name': 'w2', 'total_earnings': 30}]
        self.assertEqual([{'name': 'w1', 'total_earnings': 70}], self.restaurant.get_waiters(50, 100))

    def test_get_waiters_if_no_have_proper(self):
        self.restaurant.waiters = [{'name': 'w2', 'total_earnings': 30}]
        self.assertEqual([], self.restaurant.get_waiters(50, 100))

    def test_add_waiters_if_exist(self):
        expected = f"The waiter w1 already exists!"
        self.restaurant.waiters = [{'name': 'w1'}]
        self.assertEqual(expected, self.restaurant.add_waiter('w1'))

    def test_add_waiters_with_new_waiter(self):
        expected = f"The waiter w2 has been added."
        self.restaurant.waiters = [{'name': 'w1'}]
        self.assertEqual(expected, self.restaurant.add_waiter('w2'))
        self.assertEqual([{'name': 'w1'}, {'name': 'w2'}], self.restaurant.waiters)

    def test_add_waiters_if_no_capacity(self):
        self.restaurant.capacity = 1
        self.restaurant.waiters = [{'name': 'w1'}]
        self.assertEqual("No more places!", self.restaurant.add_waiter('w2'))

    def test_remove__waiter_if_exist(self):
        expected = f"The waiter w1 has been removed."
        self.restaurant.waiters = [{'name': 'w1'}]
        self.assertEqual(expected, self.restaurant.remove_waiter('w1'))
        self.assertEqual([], self.restaurant.waiters)

    def test_remove_waiters_if_not_exist(self):
        expected = f"No waiter found with the name w2."
        self.restaurant.waiters = [{'name': 'w1'}]
        self.assertEqual(expected, self.restaurant.remove_waiter('w2'))
        self.assertEqual([{'name': 'w1'}], self.restaurant.waiters)

    def test_get_total_earnings(self):
        self.restaurant.waiters = [{'name': 'w1', 'total_earnings': 70}, {'name': 'w2', 'total_earnings': 30}]
        self.assertEqual(100, self.restaurant.get_total_earnings())


if __name__ == "__main__":
    main()
