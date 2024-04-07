import unittest
from src.calendar_manager import export_calendar


class TestCalendarFunctions(unittest.TestCase):

    def test_load_calendar_from_json_exists(self):
        self.assertTrue(hasattr(export_calendar, 'load_calendar_from_json'))

    def test_export_to_ical_exists(self):
        self.assertTrue(hasattr(export_calendar, 'export_to_ical'))


if __name__ == '__main__':
    unittest.main()
