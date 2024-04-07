import datetime
from prettytable import PrettyTable
from googleapiclient.discovery import build
from src.helpers.common_functions import get_google_credentials
from src.helpers.date_time_utils import process_date
from src.authentification.encryption import read_email_from_file
from src.helpers.utils import clear_terminal
from src.helpers.display_graphics import print_fancy_message
from src.helpers.utils import print_red, print_green, print_yellow
from src.helpers.display_graphics import print_fancy_message
from src.calendar_manager import update_calendar
from src.helpers.common_constants import CALENDAR_ID


def load_events(service, start_date=None, end_date=None):
    """
    Load events from Google Calendar within a specified time range.

    Args:
        service (googleapiclient.discovery.Resource): The authenticated Google Calendar service.
        start_date (datetime.datetime, optional): The start date for fetching events. Defaults to None.
        end_date (datetime.datetime, optional): The end date for fetching events. Defaults to None.

    Returns:
        list: List of events fetched from Google Calendar.
    """
    time_min = start_date.isoformat(
    ) + 'Z' if start_date else datetime.datetime.utcnow().isoformat() + 'Z'
    time_max = end_date.isoformat() + 'Z' if end_date else None

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=time_min,
        timeMax=time_max,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    return events_result.get('items', [])


def add_attendee(service, event_id, attendee_email):
    """
    Add an attendee to a Google Calendar event.

    Args:
        service (googleapiclient.discovery.Resource): The authenticated Google Calendar service.
        event_id (str): The ID of the event to add the attendee to.
        attendee_email (str): The email address of the attendee to be added.
    """
    try:
        event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()

        if 'attendees' not in event:
            event['attendees'] = []

        event['attendees'].append({'email': attendee_email})

        updated_event = service.events().update(
            calendarId=CALENDAR_ID,
            eventId=event_id,
            body=event
        ).execute()

        print_green(
            f"Attendee {attendee_email} added to the event with ID: {event_id}")
        update_calendar.update_next_seven_days()
    except Exception as e:
        print_red(f"An error occurred: {e}")


def display_events(events, attendee_email):
    """
    Display events in a tabular format using PrettyTable.

    Args:
        events (list): List of events to display.
        attendee_email (str): Email of the attendee.
    """
    clear_terminal()
    table = PrettyTable()
    table.field_names = ["\033[92mEvent ID\033[0m", "\033[92mStart Date\033[0m",
                         "\033[92mStart Time\033[0m", "\033[92mLocation\033[0m", "\033[92mTopic Covered\033[0m"]

    for event in events:
        event_id = event.get('id', 'N/A')
        start_time = event['start'].get('dateTime', 'N/A')
        location = event.get('location', 'N/A')
        description = event.get('description', 'N/A')
        attendees = event.get('attendees', [])

        organizer_email = event.get('creator', {}).get('email')
        if len(attendees) == 0 and organizer_email != attendee_email:

            start_date, start_time = start_time.split('T')
            start_date_formatted = datetime.datetime.strptime(
                start_date, "%Y-%m-%d").strftime("%Y-%m-%d")

            topic_start_index = description.find("topic covered")
            notes_start_index = description.find("Notes:")
            if topic_start_index != -1 and notes_start_index != -1:
                topic_covered = description[topic_start_index +
                                            len("topic covered"): notes_start_index].strip()
            else:
                topic_covered = "N/A"

            if event_id != 'N/A':
                event_id_colored = f"\033[91m{event_id}\033[0m"  # Red color
            else:
                event_id_colored = event_id

            if location != 'N/A':
                location_colored = f"\033[91m{location}\033[0m"  # Red color
            else:
                location_colored = location

            table.add_row([event_id_colored, f"\033[92m{start_date_formatted}\033[0m",
                          f"\033[92m{start_time[:5]}\033[0m", location_colored, f"\033[92m{topic_covered}\033[0m"])

    print(table)


def main():
    """
    Main function to execute the program.
    """
    try:
        print_fancy_message("WELCOME TO OUR BOOKING SYSTEM: MAKE A BOOKING")
        print_yellow(
            "Please enter the date range to view available volunteer slots, for example, from 2024-02-01 to 2024-03-01.")
        start_date_str, end_date_str = process_date()

        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

        credentials = get_google_credentials()
        service = build('calendar', 'v3', credentials=credentials)
        attendee_email = read_email_from_file(".session.txt")
        events = load_events(service, start_date, end_date)
        display_events(events, attendee_email)

        event_id = input(
            "\033[94mEnter the event ID you want to add yourself to: \033[0m")

        add_attendee(service, event_id, attendee_email)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
