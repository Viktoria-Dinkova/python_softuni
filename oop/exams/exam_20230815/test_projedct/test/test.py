from unittest import TestCase, main

from project.trip import Trip

class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(30000.0, 3, True)

    def test_correct_init(self):
        self.assertEqual(30000.0, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_raise_valueerror_invalid_count_of_travelers(self):

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = -1
            self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_if_not_family(self):
        self.trip = Trip(7000.0, 1, True)
        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_for_nonexisting_destination(self):
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected, self.trip.book_a_trip('Uruguay'))

    def test_book_a_trip_with_low_budget(self):
        self.trip.budget = 100
        expected = 'Your budget is not enough!'
        self.assertEqual(expected, self.trip.book_a_trip("Bulgaria"))
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_successfully_book_a_trip_required_price(self):
        expected = 'Successfully booked destination New Zealand! Your budget left is 9750.00'
        result = self.trip.book_a_trip('New Zealand')

        self.assertEqual(expected, result)
        self.assertEqual({'New Zealand': 20250.00}, self.trip.booked_destinations_paid_amounts)

    def test_booking_status__no_bookings(self):
        expected = 'No bookings yet. Budget: 30000.00'
        self.assertEqual(expected, self.trip.booking_status())

    def test_booking_status_two_booking(self):
        t = Trip(30000.0, 3, True)
        t.book_a_trip('New Zealand')
        t.book_a_trip('Bulgaria')

        expected = """Booked Destination: Bulgaria
Paid Amount: 1350.00
Booked Destination: New Zealand
Paid Amount: 20250.00
Number of Travelers: 3
Budget Left: 8400.00"""

        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 1350.00, 'New Zealand': 20250.00})
        self.assertEqual(expected, t.booking_status() )


if __name__ == '__main__':
    main()