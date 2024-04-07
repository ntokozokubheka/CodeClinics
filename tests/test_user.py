import unittest
from unittest.mock import patch, MagicMock
import os
from src.authentification import user
from src.authentification import encryption


class TestAuthentificationFunctions(unittest.TestCase):

    def test_manage_user_file_imported(self):
        self.assertTrue(hasattr(user, 'manage_user_file'))

    def test_generate_key_and_save_imported(self):
        self.assertTrue(hasattr(user, 'generate_key_and_save'))

    def test_sign_up_imported(self):
        self.assertTrue(hasattr(user, 'sign_up'))

    def test_sign_in_imported(self):
        self.assertTrue(hasattr(user, 'sign_in'))

    def test_check_credentials_imported(self):
        self.assertTrue(hasattr(user, 'check_credentials'))

    def test_is_user_registered_imported(self):
        self.assertTrue(hasattr(user, 'is_user_registered'))

    def test_validate_password_imported(self):
        self.assertTrue(hasattr(user, 'validate_password'))

    def test_is_valid_email_imported(self):
        self.assertTrue(hasattr(user, 'is_valid_email'))

    def test_get_username_imported(self):
        self.assertTrue(hasattr(user, 'get_username'))

    def test_get_email_imported(self):
        self.assertTrue(hasattr(user, 'get_email'))

    def test_get_password_imported(self):
        self.assertTrue(hasattr(user, 'get_password'))

    def test_read_file_imported(self):
        self.assertTrue(hasattr(user, 'read_file'))

    def test_save_name_to_file_imported(self):
        self.assertTrue(hasattr(user, 'save_name_to_file'))


if __name__ == '__main__':
    pass