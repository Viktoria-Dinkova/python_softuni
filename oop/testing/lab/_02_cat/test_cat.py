from unittest import TestCase, main

from _02_cat.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Kitty")

    def test_correct_init(self):
        self.assertEqual("Kitty", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_size_increase_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_is_fed_after_eating(self):
        expected_fed = True

        self.cat.eat()

        self.assertEqual(expected_fed, self.cat.fed)

    def test_cannot_eat_if_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_is_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

if __name__ == "__main__":
    main()
