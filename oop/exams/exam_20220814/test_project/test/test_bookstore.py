from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(10)

    def test_init(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_raise_valueerror_if_book_limitIs_is_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_raise_valueerror_if_book_limitIs_is_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1

        self.assertEqual(f"Books limit of -1 is not valid", str(ve.exception))

    def test_len_return_total_number_of_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 1, 'second book': 2}
        result = self.bookstore.__len__()
        self.assertEqual(3, result)

    def test_receive_book_rise_exception_if_there_is_not_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 9}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('second book', 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_existence_book_with_succsses(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 9}
        expected = "10 copies of first book are available in the bookstore."
        self.assertEqual(expected, self.bookstore.receive_book('first book', 1))

    def test_receive_new_book_with_succsses(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 9}
        expected = "1 copies of second book are available in the bookstore."
        self.assertEqual(expected, self.bookstore.receive_book('second book', 1))

    def test_sell_book_raise_exception_for_not_available_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('book', 0)
        self.assertEqual("Book book doesn't exist!", str(ex.exception))

    def test_sell_book_raise_exception_for_not_enough_books(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 9}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('first book', 10)
        self.assertEqual(f"first book has not enough copies to sell. Left: 9", str(ex.exception))

    def test_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {'first book': 9}

        self.assertEqual(f"Sold 9 copies of first book", self.bookstore.sell_book('first book', 9))

    def test__str(self):
        self.bookstore.receive_book('first book', 8)
        self.bookstore.receive_book('second book', 2)
        self.bookstore.sell_book('first book', 2)
        self.bookstore.sell_book('second book', 1)

        expected = "Total sold books: 3\nCurrent availability: 7\n - first book: 6 copies\n - second book: 1 copies"

        self.assertEqual(expected, self.bookstore.__str__())


if __name__ == "__main__":
    main()
