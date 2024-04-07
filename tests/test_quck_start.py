import unittest
import src.helpers.common_functions
import src.helpers.utils
import config.quick_start


class TestCalendarFunctions(unittest.TestCase):

    def test_delete_token_file_defined(self):
        self.assertTrue(hasattr(config.quick_start, 'delete_token_file'))

    def test_config_main_defined(self):
        self.assertTrue(hasattr(config.quick_start, 'config_main'))

    def test_check_config_connection_defined(self):
        self.assertTrue(hasattr(config.quick_start, 'check_config_connection'))

    def test_print_green_defined(self):
        self.assertTrue(hasattr(src.helpers.utils, 'print_green'))

    def test_print_red_defined(self):
        self.assertTrue(hasattr(src.helpers.utils, 'print_red'))

    def test_get_google_credentials_imported(self):
        self.assertTrue(hasattr(src.helpers.common_functions,
                        'get_google_credentials'))

    def test_validate_calendar_account_imported(self):
        self.assertTrue(hasattr(src.helpers.common_functions,
                        'validate_calendar_account'))

    def test_token_file_imported(self):
        self.assertTrue(hasattr(src.helpers.common_constants, 'TOKEN_FILE'))


if __name__ == '__main__':
    unittest.main()