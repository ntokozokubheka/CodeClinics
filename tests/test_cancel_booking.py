import unittest
from src.booking_system.cancel_booking import (
    get_cancel_date,
    format_date_time,
    get_table_attendee,
    cancel_booking
)

class TestBookingFunctionsExistence(unittest.TestCase):
    def test_get_cancel_date_exists(self):
        self.assertTrue(callable(get_cancel_date))

    def test_format_date_time_exists(self):
        self.assertTrue(callable(format_date_time))

    def test_get_table_attendee_exists(self):
        self.assertTrue(callable(get_table_attendee))


    def test_cancel_booking_exists(self):
        self.assertTrue(callable(cancel_booking))

if __name__ == '__main__':
    unittest.main()
