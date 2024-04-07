import unittest
from src.calendar_manager import view_campus_schedules


class TestTextFunctions(unittest.TestCase):

    def test_wrap_text_exists(self):
        self.assertTrue(hasattr(view_campus_schedules, 'wrap_text'))

    def test_extract_topic_exists(self):
        self.assertTrue(hasattr(view_campus_schedules, 'extract_topic'))

    def test_color_red_exists(self):
        self.assertTrue(hasattr(view_campus_schedules, 'color_red'))

    def test_color_green_exists(self):
        self.assertTrue(hasattr(view_campus_schedules, 'color_green'))

    def test_display_filtered_events_exists(self):
        self.assertTrue(hasattr(view_campus_schedules,
                        'display_filtered_events'))


if __name__ == '__main__':
    unittest.main()