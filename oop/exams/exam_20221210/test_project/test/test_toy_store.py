from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_add_toy_on_non_existinct_shelf_raise_exeption(self):
        expected = "Shelf doesn't exist!"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("K", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_on_the_same_shelf_with_same_name_raise_exeption(self):
        self.store.add_toy("D", "Doly")
        expected = "Toy is already in shelf!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy(self.store.add_toy("D", "Doly"))

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual("Doly", self.store.toy_shelf['D'])

    def test_add_toy_on_the_already_taken_shelf(self):
        self.store.add_toy("D", "Doly")
        expected = "Shelf is already taken!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy(self.store.add_toy("D", "Moly"))

        self.assertEqual(expected, str(ex.exception))
        self.assertEqual("Doly", self.store.toy_shelf['D'])

    def test_add_toy_on_the_existent_free_shelf(self):
        self.store.add_toy("D", "Doly")

        expected = "Toy:dog placed successfully!"

        self.assertEqual(expected, self.store.add_toy("A", "dog"))
        # self.assertEqual("'toy_shelf': {'A': 'dog', 'B': None, 'C': None, 'D': 'Doly', 'E': None, 'F': None, 'G': None}", self.store.__dict__)

    def test_remove_toy_from_non_existinct_shelf_raise_exeption(self):
        expected = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("K", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_remove_non_existinct_toy_fron_existinct_shelf_raise_exeption(self):
        self.store.add_toy("D", "Doly")
        expected = "Toy in that shelf doesn't exists!"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("D", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_remove_with_succssess(self):
        self.store.add_toy("D", "Doly")
        expected = "Remove toy:Doly successfully!"

        self.assertEqual(expected, self.store.remove_toy("D", "Doly"))

if __name__ == '__main__':
    main()
