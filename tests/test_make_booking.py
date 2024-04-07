import unittest
from unittest.mock import MagicMock, patch
import datetime
from src.booking_system import make_booking
from src.booking_system.make_booking import main
from src.booking_system.make_booking import (
    load_events,
    add_attendee,
    display_events,
    process_date,
    
)

def process_date(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    start_date = date
    end_date = date + datetime.timedelta(days=1)
    return start_date, end_date


def load_events(arg1, start_date, end_date):
    # I am creating a list of events for my tests
    events = [
        {
            "id": 1,
            "title": "Sample Event 1",
            "description": "Sample description 1",
            "location": "Sample location 1",
            "timeMin": start_date.isoformat() + "Z",
            "timeMax": end_date.isoformat() + "Z",
            "attendees": [
                {
                    "email": "attendee1@example.com"
                }
            ]
        },
        {
            "id": 2,
            "title": "Sample Event 2",
            "description": "Sample description 2",
            "location": "Sample location 2",
            "timeMin": start_date.isoformat() + "Z",
            "timeMax": end_date.isoformat() + "Z",
            "attendees": [
                {
                    "email": "attendee2@example.com"
                }
            ]
        }
    ]
    
    return events


class TestMakeBooking(unittest.TestCase):
    def test_process_date_valid_format(self):
        date_str = "2024-03-01"
        start_date, end_date = process_date(date_str)
        assert isinstance(start_date, datetime.datetime)
        assert isinstance(end_date, datetime.datetime)
        assert start_date.strftime("%Y-%m-%d") == date_str
        
    def test_process_date_invalid_format(self):
        date_str = "01-03-2024"
        with self.assertRaises(ValueError):
            start_date, end_date = process_date(date_str)


    def test_load_events_correct_time_format(self, arg1=None):
        start_date = datetime.datetime(2024, 2, 15)
        end_date = datetime.datetime(2025, 2, 15)
        events = load_events(arg1, start_date, end_date)
        assert events[0]["timeMin"] == start_date.isoformat() + "Z"
        assert events[0]["timeMax"] == end_date.isoformat() + "Z"



    @patch('src.booking_system.make_booking.print')
    @patch('src.booking_system.make_booking.PrettyTable')
    @patch('src.booking_system.make_booking.clear_terminal')
    def test_display_events(self, mock_clear_terminal, mock_PrettyTable, mock_print):
        mock_event = {"id": "event_id", "start": {"dateTime": "2024-03-01T10:00:00"}, "location": "Test Location", "description": "Topic covered: Test Topic\nNotes: Test Notes"}
        display_events([mock_event], "test@example.com")
        mock_clear_terminal.assert_called_once()
        mock_PrettyTable.assert_called_once()
        mock_print.assert_called()

    @patch('src.booking_system.make_booking.build')
    @patch('src.booking_system.make_booking.read_email_from_file')
    @patch('src.booking_system.make_booking.process_date')
    @patch('src.booking_system.make_booking.print_fancy_message')
    @patch('src.booking_system.make_booking.print_yellow')
    @patch('src.booking_system.make_booking.load_events')
    @patch('src.booking_system.make_booking.display_events')
    @patch('src.booking_system.make_booking.input')
    @patch('src.booking_system.make_booking.add_attendee')
    def test_main_exception(self, mock_add_attendee, mock_input, mock_display_events, mock_load_events, mock_print_yellow, mock_print_fancy_message, mock_process_date, mock_read_email_from_file, mock_build):
        mock_build.side_effect = Exception("Test Exception")
        with self.assertRaises(Exception):
            main.main()

    @patch('src.booking_system.make_booking.build')
    @patch('src.booking_system.make_booking.read_email_from_file')
    @patch('src.booking_system.make_booking.process_date')
    @patch('src.booking_system.make_booking.print_fancy_message')
    @patch('src.booking_system.make_booking.print_yellow')
    @patch('src.booking_system.make_booking.load_events')
    @patch('src.booking_system.make_booking.display_events')
    @patch('src.booking_system.make_booking.input')
    @patch('src.booking_system.make_booking.add_attendee')
    def test_main_calendar_build_error(self, mock_add_attendee, mock_input, mock_display_events, mock_load_events, mock_print_yellow, mock_print_fancy_message, mock_process_date, mock_read_email_from_file, mock_build):
        mock_build.side_effect = Exception("Test Exception")
        with self.assertRaises(Exception):
            main.main()

    @patch('src.booking_system.make_booking.print')
    @patch('src.booking_system.make_booking.PrettyTable')
    @patch('src.booking_system.make_booking.clear_terminal')
    def test_display_events_no_attendees(self, mock_clear_terminal, mock_PrettyTable, mock_print):
        mock_event = {"id": "event_id", "start": {"dateTime": "2024-03-01T10:00:00"}, "location": "Test Location", "description": "Topic covered: Test Topic\nNotes: Test Notes"}
        display_events([mock_event], "test@example.com")
        mock_clear_terminal.assert_called_once()
        mock_PrettyTable.assert_called_once()
        mock_print.assert_called()

    @patch('src.booking_system.make_booking.print')
    @patch('src.booking_system.make_booking.PrettyTable')
    @patch('src.booking_system.make_booking.clear_terminal')
    def test_display_events_missing_fields(self, mock_clear_terminal, mock_PrettyTable, mock_print):
        mock_event = {"id": "event_id", "start": {"dateTime": "2024-03-01T10:00:00"}, "description": "Test Description"}
        display_events([mock_event], "test@example.com")
        mock_clear_terminal.assert_called_once()
        mock_PrettyTable.assert_called_once()
        mock_print.assert_called()

    @patch('src.booking_system.make_booking.get_google_credentials')
    @patch('src.booking_system.make_booking.build')
    @patch('src.booking_system.make_booking.read_email_from_file')
    @patch('src.booking_system.make_booking.process_date')
    @patch('src.booking_system.make_booking.print_fancy_message')
    @patch('src.booking_system.make_booking.print_yellow')
    @patch('src.booking_system.make_booking.load_events')
    @patch('src.booking_system.make_booking.display_events')
    @patch('src.booking_system.make_booking.input')
    @patch('src.booking_system.make_booking.add_attendee')
    def test_successful_booking(self, mock_add_attendee, mock_input, mock_display_events, mock_load_events, mock_print_yellow, mock_print_fancy_message, mock_process_date, mock_read_email_from_file, mock_build, mock_get_google_credentials):

        mock_service = MagicMock()
        mock_build.return_value = mock_service
        mock_get_google_credentials.return_value = MagicMock()
        mock_read_email_from_file.return_value = "test@example.com"
        mock_process_date.return_value = ("2024-02-01", "2024-03-01")
        mock_input.return_value = "event_id"
        mock_load_events.return_value = [{"id": "event_id", "start": {"dateTime": "2024-03-01T10:00:00"}, "location": "Test Location", "description": "Test Description"}]

        make_booking.main()

        mock_build.assert_called_once_with('calendar', 'v3', credentials=mock_get_google_credentials.return_value)
        mock_read_email_from_file.assert_called_once_with(".session.txt")
        mock_process_date.assert_called_once()
        mock_print_fancy_message.assert_called_once()
        mock_print_yellow.assert_called_once()
        mock_load_events.assert_called_once()
        mock_display_events.assert_called_once()
        mock_input.assert_called_once()
        mock_add_attendee.assert_called_once_with(mock_service, "event_id", "test@example.com")
        mock_display_events.assert_called_once()
        mock_print_yellow.assert_called_once()
        mock_print_fancy_message.assert_called_once()


    @patch('src.booking_system.make_booking.print_red')
    def test_add_attendee_error(self, mock_print_red):
        mock_service = MagicMock()
        mock_event_id = 'event_id'
        mock_attendee_email = 'test@example.com'
        mock_service.events().get().execute.side_effect = Exception('Test error')
        add_attendee(mock_service, mock_event_id, mock_attendee_email)
        mock_print_red.assert_called_once_with("An error occurred: Test error")



if __name__ == '__main__':
    unittest.main()