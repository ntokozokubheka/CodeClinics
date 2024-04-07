import unittest
import sys
from src.cli.command_line import (
    manage_authentication, manage_student, manage_volunteer,
    manage_calendar, export_calendar, update_calendar,
    check_configured_connection, configure_connection,
    help_menu, volunteer_a_slot, cancel_volunteer_slot,
    cancel_a_booking, make_a_booking, sign_out_session,
    view_calendar, view_my_bookings
)

class TestFunctionsExistence(unittest.TestCase):

    def test_manage_authentication_exists(self):
        self.assertTrue(callable(manage_authentication))

    def test_manage_student_exists(self):
        self.assertTrue(callable(manage_student))

    def test_manage_volunteer_exists(self):
        self.assertTrue(callable(manage_volunteer))

    def test_manage_calendar_exists(self):
        self.assertTrue(callable(manage_calendar))

    def test_export_calendar_exists(self):
        self.assertTrue(callable(export_calendar))

    def test_update_calendar_exists(self):
        self.assertTrue(callable(update_calendar))

    def test_check_configured_connection_exists(self):
        self.assertTrue(callable(check_configured_connection))

    def test_configure_connection_exists(self):
        self.assertTrue(callable(configure_connection))

    def test_help_menu_exists(self):
        self.assertTrue(callable(help_menu))

    def test_volunteer_a_slot_exists(self):
        self.assertTrue(callable(volunteer_a_slot))

    def test_cancel_volunteer_slot_exists(self):
        self.assertTrue(callable(cancel_volunteer_slot))

    def test_cancel_a_booking_exists(self):
        self.assertTrue(callable(cancel_a_booking))

    def test_make_a_booking_exists(self):
        self.assertTrue(callable(make_a_booking))

    def test_sign_out_session_exists(self):
        self.assertTrue(callable(sign_out_session))

    def test_view_calendar_exists(self):
        self.assertTrue(callable(view_calendar))

    def test_view_my_bookings_exists(self):
        self.assertTrue(callable(view_my_bookings))

if __name__ == '__main__':
    unittest.main()
