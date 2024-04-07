import unittest
from src.helpers.common_functions import (
    validate_calendar_account,
    get_google_credentials,
    get_user_email
)


class TestCalendarFunctionsExistence(unittest.TestCase):
    def test_validate_calendar_account_exists(self):
        self.assertTrue(callable(validate_calendar_account))

    def test_get_google_credentials_exists(self):
        self.assertTrue(callable(get_google_credentials))

    def test_get_user_email_exists(self):
        self.assertTrue(callable(get_user_email))


if __name__ == '__main__':
    unittest.main()