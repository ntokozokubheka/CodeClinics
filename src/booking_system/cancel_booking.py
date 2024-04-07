import datetime
import pytz
from tabulate import tabulate
from src.authentification.encryption import read_email_from_file
from src.helpers.common_constants import CALENDAR_ID, Calender_Timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.helpers.display_graphics import print_fancy_message
from src.helpers.common_constants import TOKEN_FILE
from src.helpers.utils import print_red, print_yellow, print_green
from src.helpers.common_functions import get_google_credentials
from src.calendar_manager import update_calendar


def get_cancel_date():
    """
    Prompt the user to input a booking date and time and return it in UTC format.

    Returns:
        str: The booking date and time in UTC format.
    """
    while True:
        booking_date_input = input(
            "\033[94mPlease enter booking date in this format (YYYY-MM-DD): \033[0m").strip()

        try:
            booking_date = datetime.datetime.strptime(
                booking_date_input, '%Y-%m-%d').date()
            break
        except ValueError:
            print_red(
                "This date format is invalid. Please enter the correct date in this YYYY-MM-DD format.")

    while True:
        booking_time_input = input(
            "\033[94mPlease enter the booking time in this format (HH:MM): \033[0m").strip()

        try:
            booking_time = datetime.datetime.strptime(
                booking_time_input, '%H:%M').time()
            break
        except ValueError:
            print_red(
                "This time format is invalid. Please enter the correct time in this HH:MM format.")

    booking_datetime = datetime.datetime.combine(booking_date, booking_time)
    booking_datetime_utc = pytz.timezone(Calender_Timezone).localize(
        booking_datetime).astimezone(pytz.utc)

    start_datetime = booking_datetime_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    return start_datetime


def format_date_time(raw_date_time):
    """
    Convert raw date and time string to a formatted date and time string.

    Args:
        raw_date_time (str): The raw date and time string.

    Returns:
        str: The formatted date and time string.
    """
    dt_object = datetime.datetime.fromisoformat(raw_date_time)
    formatted_date_time = dt_object.strftime('%Y-%m-%d %H:%M')
    return formatted_date_time


def get_table_attendee(user_email, creds):
    """
    Retrieve and format the user's booked slots into a tabular format.

    Args:
        user_email (str): The email address of the user.
        creds: The user's Google Calendar credentials.

    Returns:
        str: The tabulated representation of the user's booked slots.
    """
    service = build("calendar", "v3", credentials=creds)

    print_yellow("THE SLOTS YOU BOOKED ARE:")

    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now,
                                              maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print_red('No upcoming events found.')
            return

        matching_events = []

        for event in events:
            attendees_emails = [attendee.get('email')
                                for attendee in event.get('attendees', [])]
            summary = event.get('summary', '')

            if user_email in attendees_emails and 'volunteer' in summary.lower():
                formatted_date_time = format_date_time(
                    event['start']['dateTime'])
                matching_events.append([formatted_date_time, summary])

        headers = ['Date and Time', 'Event Summary']
        table = tabulate(matching_events, headers=headers, tablefmt='pretty')
        return table

    except HttpError as error:
        return (f"An error occurred: {error}")


def do_cancelation(start_datetime, user_email, creds):
    """
    Cancel a booking based on the provided start date and time.

    Args:
        start_datetime (str): The start date and time of the booking.
        user_email (str): The email address of the user.
        creds: The user's Google Calendar credentials.

    Returns:
        str: A message indicating the cancellation status.
    """
    service = build("calendar", "v3", credentials=creds)
    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now,
                                              maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        for event in events:
            if 'dateTime' in event['start']:
                event_start = datetime.datetime.strptime(
                    event['start']['dateTime'], '%Y-%m-%dT%H:%M:%S%z')
            elif 'date' in event['start']:
                event_start = datetime.datetime.strptime(
                    event['start']['date'], '%Y-%m-%d')

            event_start_utc = event_start.astimezone(pytz.utc)

            if event_start_utc.strftime('%Y-%m-%dT%H:%M:%SZ') == start_datetime:
                wrong_name = False
                try:
                    wrong_name = True
                    new_attendees = []

                    for attendee in event.get('attendees', []):
                        if attendee.get('email') == user_email:
                            print_green(
                                "Attendee removed from the event successfully.")
                            update_calendar.update_next_seven_days()
                            wrong_name = False
                        else:
                            new_attendees.append(attendee)

                    if not wrong_name:
                        event['attendees'] = new_attendees

                        service.events().update(calendarId=CALENDAR_ID,
                                                eventId=event['id'], body=event).execute()
                    else:
                        print_red(
                            "You can't delete bookings that aren't in your name")

                except HttpError as error:
                    print_red(f"An error occurred: {error}")

            else:
                return ("No booking for that time in your name")
    except HttpError as error:
        print_red(f"An error occurred: {error}")


def cancel_booking():
    """
    Cancel a booking for the current user.
    """
    print_fancy_message("WELCOME TO OUR BOOKING SYSTEM : CANCEL BOOKING")

    user_email = read_email_from_file(".session.txt")

    creds = get_google_credentials()

    table = get_table_attendee(user_email, creds)
    print(table)
    print()

    start_datetime = get_cancel_date()

    do_cancelation(start_datetime, user_email, creds)
