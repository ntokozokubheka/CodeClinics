import unittest
from unittest.mock import patch
from src.helpers.assign_location import get_location


class TestGetLocation(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1'])
    def test_get_location_jhb_main(self, mock_input):
        location = get_location()
        self.assertEqual(location, "Jhb main, 4-Robotics Lab (2)")

    @patch('builtins.input', side_effect=['5'])
    def test_get_location_online(self, mock_input):
        location = get_location()
        self.assertEqual(location, "Online")


if __name__ == '__main__':
    unittest.main()