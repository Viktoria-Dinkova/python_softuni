from project.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library('mine')

    def test_correct_init(self):
        self.assertEqual('mine', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_raise_valueerror_if_library_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_from_new_author(self):
        self.library.add_book('me', 'my book')
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue('me' in self.library.books_by_authors)
        self.assertEqual(['my book'], self.library.books_by_authors['me'])

    def test_add_book_from_existing_author(self):
        self.library.add_book('me', 'my book')
        self.library.add_book('me', 'my second book')
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue('me' in self.library.books_by_authors)
        self.assertEqual(['my book', 'my second book'], self.library.books_by_authors['me'])

    def test_add_existing_book(self):
        self.library.add_book('me', 'my book')
        self.library.add_book('me', 'my book')
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue('me' in self.library.books_by_authors)
        self.assertEqual(['my book'], self.library.books_by_authors['me'])

    def test_add_reader_newone(self):
        self.library.add_reader('me')
        self.assertEqual(1, len(self.library.readers))
        self.assertTrue('me' in self.library.readers)
        self.assertEqual([], self.library.readers['me'])

    def test_add_reader_again(self):
        self.library.add_reader('me')
        self.assertEqual('me is already registered in the mine library.', self.library.add_reader('me'))
        self.assertEqual(1, len(self.library.readers))
        self.assertTrue('me' in self.library.readers)
        self.assertEqual([], self.library.readers['me'])

    def test_rent_book_return_message_for_noexistinct_reader(self):
        self.assertEqual("me is not registered in the mine Library.", self.library.rent_book('me', 'you', '3'))

    def test_rent_book_return_message_for_noexistinct_author(self):
        self.library.add_reader('me')
        self.library.add_book('you', 'your book')
        self.assertEqual("mine Library does not have any she's books.", self.library.rent_book('me', 'she', '3'))

    def test_rent_book_return_message_for_noexistinct_book(self):
        self.library.add_reader('me')
        self.library.add_book('you', 'your book')
        self.assertEqual('mine Library does not have you\'s "3".', self.library.rent_book('me', 'you', '3'))

    def test_rent_book_correct(self):
        self.library.add_reader('me')
        self.library.add_book('you', 'your book')
        self.library.rent_book('me', 'you', 'your book')

        self.assertEqual(1, len(self.library.readers['me']))
        self.assertFalse('you' not in self.library.books_by_authors)


if __name__ == '__main__':
    main()
