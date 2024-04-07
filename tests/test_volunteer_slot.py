import unittest
from src.booking_system import volunteer_slot


class TestVolunteerSlotFunctions(unittest.TestCase):

    def test_convert_to_johannesburg_time_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'convert_to_johannesburg_time'))

    def test_check_double_booking_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'check_double_booking'))

    def test_construct_event_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'construct_event'))

    def test_add_conference_data_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'add_conference_data'))

    def test_add_recurrence_rule_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'add_recurrence_rule'))

    def test_insert_event_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'insert_event'))

    def test_book_slot_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'book_slot'))

    def test_get_user_input_full_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'get_user_input_full'))

    def test_print_event_details_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'print_event_details'))

    def test_main_imported(self):
        self.assertTrue(hasattr(
            volunteer_slot, 'main'))


if __name__ == '__main__':
    unittest.main()