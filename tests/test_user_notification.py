import unittest
from unittest.mock import patch
from src.helpers.user_notification_preferences import (
    email_notification_validation,
    pop_up_notification_validation,
    recurring_event_validation,
    notes_validation
)


class TestValidationFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_email_notification_validation_yes(self, mock_input):
        self.assertTrue(email_notification_validation())

    @patch('builtins.input', side_effect=['n'])
    def test_email_notification_validation_no(self, mock_input):
        self.assertFalse(email_notification_validation())

    @patch('builtins.input', side_effect=['y'])
    def test_pop_up_notification_validation_yes(self, mock_input):
        self.assertTrue(pop_up_notification_validation())

    @patch('builtins.input', side_effect=['n'])
    def test_pop_up_notification_validation_no(self, mock_input):
        self.assertFalse(pop_up_notification_validation())

    @patch('builtins.input', side_effect=['y', 'daily'])
    def test_recurring_event_validation_yes_daily(self, mock_input):
        recurring, recurrence = recurring_event_validation()
        self.assertEqual(recurring, 'y')
        self.assertEqual(recurrence, 'daily')

    @patch('builtins.input', side_effect=['y', 'weekly'])
    def test_recurring_event_validation_yes_weekly(self, mock_input):
        recurring, recurrence = recurring_event_validation()
        self.assertEqual(recurring, 'y')
        self.assertEqual(recurrence, 'weekly')

    @patch('builtins.input', side_effect=['y', 'monthly'])
    def test_recurring_event_validation_yes_monthly(self, mock_input):
        recurring, recurrence = recurring_event_validation()
        self.assertEqual(recurring, 'y')
        self.assertEqual(recurrence, 'monthly')

    @patch('builtins.input', side_effect=['n', None])
    def test_recurring_event_validation_no(self, mock_input):
        recurring, recurrence = recurring_event_validation()
        self.assertIsNone(recurring)
        self.assertIsNone(recurrence)

    @patch('builtins.input', side_effect=['n'])
    def test_notes_validation_no(self, mock_input):
        notes = notes_validation()
        self.assertIsNone(notes)


if __name__ == '__main__':
    unittest.main()
