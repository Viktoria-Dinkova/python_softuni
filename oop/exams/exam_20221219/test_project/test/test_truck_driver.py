from unittest import TestCase, main

from test_project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("Gosho", 1)

    def test_correct_init(self):
        self.assertEqual("Gosho", self.truck_driver.name)
        self.assertEqual(1, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_driver_owes_money(self):
        expected = f"{self.truck_driver.name} went bankrupt."
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -2

        self.assertEqual(expected, str(ve.exception))

    def test_add_new_cargo(self):
        expected = f"Cargo for 45 to Sofia was added as an offer."

        self.assertEqual(expected, self.truck_driver.add_cargo_offer('Sofia', 45))
        self.assertEqual({'Sofia': 45}, self.truck_driver.available_cargos)

    def test_add_an_existence_cargo_raise_exception(self):
        self.truck_driver.add_cargo_offer('Sofia', 45)
        expected = "Cargo offer is already added."

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer('Sofia', 44)

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual({'Sofia': 45}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer_with_no_cargos(self):
        expected = "There are no offers available."

        self.assertEqual(expected, self.truck_driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offer(self):
        self.truck_driver.add_cargo_offer('Sofia', 45)
        self.truck_driver.add_cargo_offer('Varna', 450)

        expected = f"{self.truck_driver.name} is driving 450 to Varna."

        self.assertEqual(expected, self.truck_driver.drive_best_cargo_offer())
        self.assertEqual(430, self.truck_driver.earned_money)
        self.assertEqual(450, self.truck_driver.miles)

    def test_eat(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        self.truck_driver.eat(500)

        self.assertEqual(self.truck_driver.earned_money, 60)

    def test_sleep(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(self.truck_driver.earned_money, 10)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def repair_truck(self):
        self.truck_driver.earned_money = 16000

        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repr(self):
        self.assertEqual(str(self.truck_driver), "Gosho has 0 miles behind his back.")


if __name__ == "__main__":
    main()
