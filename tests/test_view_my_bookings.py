import unittest
from src.calendar_manager import view_my_bookings


class TestTextFunctions(unittest.TestCase):

    def test_wrap_text_exists(self):
        self.assertTrue(hasattr(view_my_bookings, 'wrap_text'))

    def test_extract_topic_exists(self):
        self.assertTrue(hasattr(view_my_bookings, 'extract_topic'))

    def test_color_red_exists(self):
        self.assertTrue(hasattr(view_my_bookings, 'color_red'))

    def test_color_green_exists(self):
        self.assertTrue(hasattr(view_my_bookings, 'color_green'))

    def test_display_filtered_events_exists(self):
        self.assertTrue(hasattr(view_my_bookings,
                        'display_filtered_events'))


if __name__ == '__main__':
    unittest.main()