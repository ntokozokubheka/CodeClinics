from googleapiclient.discovery import build
from prettytable import PrettyTable
from datetime import datetime, timedelta
from src.helpers.common_functions import get_google_credentials, validate_calendar_account, read_email_from_file
from src.helpers.date_time_utils import process_date
from src.calendar_manager import update_calendar
from src.helpers.utils import clear_terminal
import os
from src.helpers.utils import print_red, print_yellow, print_green
from src.helpers.display_graphics import print_fancy_message


def get_events_for_date_range(start_date, end_date):
    """
    Retrieve and display events from the specified Google Calendar for a given date range.

    Args:
        start_date (str): The start date of the range in YYYY-MM-DD format.
        end_date (str): The end date of the range in YYYY-MM-DD format.
    """
    creds = get_google_credentials()

    organizer_email = validate_calendar_account(creds)
    service = build("calendar", "v3", credentials=creds)
    calendar_id = 'c_cbaa9da597b10a5784f3eb622af3230ea534be93ca34f77b175ef0a411c1a7d1@group.calendar.google.com'

    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")

    end_datetime = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)

    start_time = start_datetime.isoformat() + 'Z'
    end_time = end_datetime.isoformat() + 'Z'

    try:
        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
        ).execute()

        events = events_result.get('items', [])

        if events:
            print("\033[92mEvents for the date range:\033[0m")

            print_events_table(events, organizer_email)
            event_id_to_delete = input(
                "\033[94mEnter the ID of the event you want to delete: \033[0m")

            if check_attendees_presence(service, calendar_id, event_id_to_delete, "@student.wethinkcode.co.za"):
                delete_event(service, calendar_id, event_id_to_delete)
            else:
                print_red("Attendees are present. Cannot delete the event.")

        else:
            print_red("No events found for the specified date range.")

    except Exception as e:
        print_red("An error occurred while retrieving events: {}".format(str(e)))


def check_attendees_presence(service, calendar_id, event_id, domain):
    """
    Check if attendees' email addresses contain the specified domain.

    Args:
        service: The Google Calendar API service object.
        calendar_id (str): The ID of the calendar.
        event_id (str): The ID of the event to check.
        domain (str): The domain to check for in attendees' email addresses.

    Returns:
        bool: True if all attendees have email addresses with the specified domain, False otherwise.
    """
    try:
        event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        attendees = event.get('attendees', [])

        if attendees:
            for attendee in attendees:
                print(attendee)
                email = attendee.get('email')
                if email and email.endswith(domain):
                    return False
        return True
    except Exception as e:
        print_red(
            "An error occurred while fetching event details: {}".format(str(e)))

        return False


def print_events_table(events, organizer_email):
    """
    Print a formatted table of events.

    Args:
        events (list): A list of event dictionaries.
    """
    clear_terminal()

    table = PrettyTable()
    table.field_names = ["Event ID", "Description",
                         "Start Time", "End Time", "Location"]

    colored_field_names = [
        f"\033[93m{name}\033[0m" for name in table.field_names]
    table.field_names = colored_field_names

    events.sort(key=lambda event: event.get('start', {}).get('dateTime', ''))

    terminal_width = os.get_terminal_size().columns

    for event in events:
        creator_in_event = event.get('creator', {}).get('email', '')
        if organizer_email == creator_in_event:
            event_id = event.get('id')
            description = event.get('description', 'No description')
            start_time = event.get('start', {}).get(
                'dateTime', 'No start time')
            end_time = event.get('end', {}).get('dateTime', 'No end time')
            location = event.get('location', 'No location')

            colored_event_id = f"\033[92m{str(event_id)}\033[0m"
            colored_description = f"\033[92m{str(description)}\033[0m"
            colored_start_time = f"\033[92m{start_time}\033[0m"
            colored_end_time = f"\033[92m{end_time}\033[0m"
            colored_location = f"\033[92m{location}\033[0m"

            table.add_row([colored_event_id, colored_description,
                           colored_start_time, colored_end_time, colored_location])

            table.add_row(["", "", "", "", ""])

    column_width = terminal_width // len(table.field_names)
    for field in table.field_names:
        table.align[field] = 'l'
        table.max_width[field] = column_width

    print(table)


def delete_event(service, calendar_id, event_id):
    """
    Delete a specific event from the user's Google Calendar.

    Args:
        service: The Google Calendar API service object.
        calendar_id (str): The ID of the calendar.
        event_id (str): The ID of the event to be deleted.
    """
    try:
        service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
        print_green("Event with ID {} deleted successfully.".format(event_id))

        update_calendar.update_next_seven_days()

    except Exception as e:
        print_red("An error occurred while deleting the event: {}".format(str(e)))


def main():
    """
    Main function to retrieve and display events from the user's Google Calendar.
    """
    print_fancy_message("WELCOME TO OUR VOLUNTEER SYSTEM: CANCEL A BOOKING")
    print_yellow(
        "Please enter the date range to view slots you've created, for example, from 2024-02-01 to 2024-03-01.")
    start_date, end_date = process_date()
    get_events_for_date_range(start_date, end_date)
