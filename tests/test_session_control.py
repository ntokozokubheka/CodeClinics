import unittest
from unittest.mock import patch, MagicMock
import os
from src.helpers.utils import print_red, print_green, clear_terminal
from src.authentification.session_control import read_file, save_user_to_file, sign_out, check_user_session
import src.authentification.session_control

class TestFileOperations(unittest.TestCase):


    def test_read_file_existing_file(self):
          self.assertTrue(hasattr(src.authentification.session_control, 'save_user_to_file'))

    def test_read_file_non_existing_file(self):
        content = read_file("non_existing_file.txt")
        self.assertFalse(content)


    @patch('src.authentification.session_control.clear_terminal')
    @patch('builtins.print')
    def test_sign_out(self, mock_print, mock_clear_terminal):
        sign_out()
        mock_clear_terminal.assert_called_once()
        mock_print.assert_called_once_with('\033[92mSuccessfully signed out\033[0m')

    @patch('src.authentification.session_control.read_file', return_value="John")
    def test_check_user_session_with_user(self, mock_read_file):
        is_user, username = check_user_session()
        self.assertTrue(is_user)
        self.assertEqual(username, "John")

    @patch('src.authentification.session_control.read_file', return_value=None)
    def test_check_user_session_no_user(self, mock_read_file):
        is_user, username = check_user_session()
        self.assertFalse(is_user)
        self.assertEqual(username, "No User Found")


if __name__ == '__main__':
    unittest.main()