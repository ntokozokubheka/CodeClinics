import unittest
from unittest.mock import patch, MagicMock
from src.calendar_manager import view_calendar


class TestCalendarFunctions(unittest.TestCase):

    def test_view_calendar_imported(self):
        self.assertTrue(hasattr(view_calendar, 'view_calendar'))


if __name__ == '__main__':
    unittest.main()