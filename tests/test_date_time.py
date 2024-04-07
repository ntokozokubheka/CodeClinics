import unittest
from src.helpers.date_time_utils import (
    validate_single_date,
    validate_date_format,
    is_start_date_before_end_date,
    process_date,
    validate_time,
    validate_work_hours,
    is_sunday,
    is_sa_public_holiday,
    get_johannesburg_date,
    is_regular_day
)

class TestDateUtilsFunctionsExistence(unittest.TestCase):
    def test_validate_single_date_exists(self):
        self.assertTrue(callable(validate_single_date))

    def test_validate_date_format_exists(self):
        self.assertTrue(callable(validate_date_format))

    def test_is_start_date_before_end_date_exists(self):
        self.assertTrue(callable(is_start_date_before_end_date))

    def test_process_date_exists(self):
        self.assertTrue(callable(process_date))

    def test_validate_time_exists(self):
        self.assertTrue(callable(validate_time))

    def test_validate_work_hours_exists(self):
        self.assertTrue(callable(validate_work_hours))

    def test_is_sunday_exists(self):
        self.assertTrue(callable(is_sunday))

    def test_is_sa_public_holiday_exists(self):
        self.assertTrue(callable(is_sa_public_holiday))

    def test_get_johannesburg_date_exists(self):
        self.assertTrue(callable(get_johannesburg_date))

    def test_is_regular_day_exists(self):
        self.assertTrue(callable(is_regular_day))

if __name__ == '__main__':
    unittest.main()