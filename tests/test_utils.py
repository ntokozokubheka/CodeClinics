import unittest
from src.helpers.utils import (
    print_green,
    print_red,
    print_yellow,
    validate_name,
    validate_surname,
    clear_terminal,
    create_hidden_text_files_in_home,
    check_alphabets
)

class TestUtilsFunctionsExistence(unittest.TestCase):
    def test_print_green_exists(self):
        self.assertTrue(callable(print_green))

    def test_print_red_exists(self):
        self.assertTrue(callable(print_red))

    def test_print_yellow_exists(self):
        self.assertTrue(callable(print_yellow))

    def test_validate_name_exists(self):
        self.assertTrue(callable(validate_name))

    def test_validate_surname_exists(self):
        self.assertTrue(callable(validate_surname))

    def test_clear_terminal_exists(self):
        self.assertTrue(callable(clear_terminal))

    def test_create_hidden_text_files_in_home_exists(self):
        self.assertTrue(callable(create_hidden_text_files_in_home))

    def test_check_alphabets_exists(self):
        self.assertTrue(callable(check_alphabets))

if __name__ == '__main__':
    unittest.main()
