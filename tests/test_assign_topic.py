import unittest
from unittest.mock import patch
from src.helpers.assign_topic import select_session


class TestSelectSession(unittest.TestCase):

    @patch('builtins.input', side_effect=['general', '1'])
    def test_select_session_general(self, mock_input):
        topic = select_session()
        self.assertEqual(topic, "Variable declaration")


if __name__ == '__main__':
    unittest.main()