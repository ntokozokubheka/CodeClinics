import unittest
from src.booking_system import cancel_volunteer


class TestVolunteerSlotFunctions(unittest.TestCase):

    def test_get_events_for_date_range_imported(self):
        self.assertTrue(hasattr(
            cancel_volunteer, 'get_events_for_date_range'))

    def test_check_attendees_presence_imported(self):
        self.assertTrue(hasattr(
            cancel_volunteer, 'check_attendees_presence'))

    def test_print_events_table_imported(self):
        self.assertTrue(hasattr(
            cancel_volunteer, 'print_events_table'))

    def test_delete_event_imported(self):
        self.assertTrue(hasattr(
            cancel_volunteer, 'delete_event'))

    def test_main_imported(self):
        self.assertTrue(hasattr(
            cancel_volunteer, 'main'))


if __name__ == '__main__':
    unittest.main()