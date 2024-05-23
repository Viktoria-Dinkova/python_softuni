from unittest import TestCase, main

from prioject.movie import Movie


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("it", 1993, 9.5)

    def test_init(self):
        self.assertEqual('it', self.movie.name)
        self.assertEqual(1993, self.movie.year)
        self.assertEqual(9.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_miss_name_raise_valuerror(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_wrong_year_raise_valuerror(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_twice_failed(self):
        self.movie.actors = ['gosho']
        self.assertEqual(f"gosho is already added in the list of actors!", self.movie.add_actor("gosho"))

    def test_add_actor_with_success(self):
        self.movie.actors = ['gosho']
        self.movie.add_actor("tosho")
        self.assertEqual(['gosho', 'tosho'], self.movie.actors)

    def test_gt_if_true(self):
        self.other = Movie('others', 1993, 9.3)
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other.name}"', self.movie > self.other)

    def test_gt_if_false(self):
        self.other = Movie('others', 1993, 10.0)
        self.assertEqual(f'"{self.other.name}" is better than "{self.movie.name}"', self.movie > self.other)

    def test_gt_false_if_equal(self):
        self.other = Movie('others', 1993, 9.5)
        self.assertEqual(f'"{self.other.name}" is better than "{self.movie.name}"', self.movie > self.other)

    def test_repr(self):
        expected = f"Name: it\nYear of Release: 1993\nRating: 9.50\nCast: gosho, tosho"
        self.movie.actors = ['gosho', 'tosho']
        self.assertEqual(expected, str(self.movie))


if __name__ == "__main__":
    main()
