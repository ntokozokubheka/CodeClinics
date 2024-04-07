import unittest
from src.calendar_manager import update_calendar


class TestCalendarFunctions(unittest.TestCase):

    def test_fetch_calendar_events_exists(self):
        self.assertTrue(hasattr(update_calendar, 'fetch_calendar_events'))

    def test_save_data_to_file_exists(self):
        self.assertTrue(hasattr(update_calendar, 'save_data_to_file'))

    def test_update_next_seven_days_exists(self):
        self.assertTrue(hasattr(update_calendar, 'update_next_seven_days'))

    def test_personal_update_exists(self):
        self.assertTrue(hasattr(update_calendar, 'personal_update'))


if __name__ == '__main__':
    unittest.main()