
from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar('wv', 'van', 50000, 10000)

    def test_init(self):
        self.assertEqual('wv', self.car.model)
        self.assertEqual('van', self.car.car_type)
        self.assertEqual(50000, self.car.mileage)
        self.assertEqual(10000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_raise_valueerror_low_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_raise_valueerror_low_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_raise_valueerror_with_high_promotional_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(12000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_correct_valid_promotional_price(self):
        self.assertEqual('The promotional price has been successfully set.', self.car.set_promotional_price(5000))

    def test_impossible_repair_because_of_high_prise(self):

        self.assertEqual('Repair is impossible!', self.car.need_repair(5001, 'engine'))


    def test_repair_with_succsses(self):
        self.assertEqual(f'Price has been increased due to repair charges.', self.car.need_repair(4999, 'engine'))
        self.assertEqual(14999, self.car.price)
        self.assertEqual(['engine'], self.car.repairs)

    def test_gt_false_different_type(self):
        self.other = SecondHandCar('wv', 'car', 50000, 10000)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car.__gt__(self.other))


    def test_gt_is_true(self):
        self.other = SecondHandCar('wv', 'car', 50000, 9999)
        self.assertTrue(self.car.__gt__(self.other))


    def test_gt_is_false(self):
        self.other = SecondHandCar('wv', 'car', 50000, 10000)
        self.assertTrue(self.car.__gt__(self.other))

    def test_str(self):
        expected = f"""Model wv | Type van | Milage 50000km
Current price: 14999.00 | Number of Repairs: 1"""
        self.car.need_repair(4999, 'engine')

        self.assertEqual(expected, self.car.__str__())


if __name__ == "__main__":
    main()
