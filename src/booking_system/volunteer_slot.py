import pytz
import datetime
from googleapiclient.discovery import build
from prettytable import PrettyTable
from src.helpers.common_functions import get_google_credentials, validate_calendar_account
from src.calendar_manager import update_calendar
from src.helpers.date_time_utils import validate_single_date, validate_time
from src.helpers.user_notification_preferences import email_notification_validation, pop_up_notification_validation, notes_validation, recurring_event_validation
from src.helpers.utils import validate_name, validate_surname, clear_terminal, print_yellow, print_green, print_red, check_alphabets
from src.helpers.assign_location import get_location
from src.helpers.assign_topic import select_session
from src.helpers.common_constants import CALENDAR_ID
from src.helpers.display_graphics import print_fancy_message


def convert_to_johannesburg_time(datetime_str):
    datetime_obj = datetime.datetime.strptime(
        datetime_str, '%Y-%m-%dT%H:%M:%S')

    johannesburg_tz = pytz.timezone('Africa/Johannesburg')

    datetime_obj = johannesburg_tz.localize(datetime_obj)
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%S%z')


def check_double_booking(service, start_datetime, end_datetime, location):
    try:
        start_time_iso = convert_to_johannesburg_time(start_datetime)
        end_time_iso = convert_to_johannesburg_time(end_datetime)

        events_result = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start_time_iso,
            timeMax=end_time_iso,
            singleEvents=True
        ).execute()
        events = events_result.get('items', [])

        if events:
            for event in events:
                if ((start_time_iso <= event['end']['dateTime'] and
                        end_time_iso >= event['start']['dateTime']) and (not check_alphabets(location, event.get('location', None)))):
                    print_red(
                        "There is a conflicting event at the same time and location. Double booking prevented.")
                    return False
            print_red(
                "There is a conflicting event at the same time and location. Double booking prevented.")
            return False
        else:
            return True
    except Exception as e:
        print_red(f"An error occurred while checking double booking: {e}")
        return False


def construct_event(volunteer_name, volunteer_topic, location, start_time, end_time, recurrence, notes):
    event = {
        'summary': 'Coding Clinic Volunteer Slot',
        'description': f'Volunteering for coding clinic by {volunteer_name} and topic covered {volunteer_topic}. Notes: {notes}',
        'start': {
            'dateTime': start_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'location': location,
        'reminders': {
            'useDefault': False,
            'overrides': []
        }
    }
    return event


def add_conference_data(event, location):
    if location.lower() == 'online':
        event['conferenceData'] = {
            'createRequest': {
                'requestId': 'meet'
            }
        }


def add_recurrence_rule(event, recurring, recurrence):
    if recurring:
        event['recurrence'] = [
            f'RRULE:FREQ={recurrence.upper()}'
        ]


def insert_event(service, event, calendar_id):
    try:
        event = service.events().insert(
            calendarId=calendar_id,
            body=event,
            conferenceDataVersion=1,
        ).execute()
        print_green(f"Event created: {event.get('htmlLink')}")
        if calendar_id != "primary":
            print_event_details(event)
            update_calendar.update_next_seven_days()
    except Exception as e:
        print_red(f"An error occurred while booking slot: {e}")


def book_slot(volunteer_name, start_datetime, end_datetime, location, volunteer_topic, email_notification, popup_notification, recurring, recurrence, notes):

    creds = get_google_credentials()

    validate_calendar_account(creds)

    service = build("calendar", "v3", credentials=creds)

    start_time = convert_to_johannesburg_time(start_datetime)
    end_time = convert_to_johannesburg_time(end_datetime)

    event = construct_event(volunteer_name, volunteer_topic,
                            location, start_time, end_time, recurrence, notes)

    add_conference_data(event, location)

    add_recurrence_rule(event, recurring, recurrence)
    if check_double_booking(service, start_datetime, end_datetime, location):
        insert_event(service, event, CALENDAR_ID)
        insert_event(service, event, "primary")


def get_user_input_full():
    name = validate_name()
    surname = validate_surname()
    volunteer_topic = select_session()
    date_input = validate_single_date()
    start_time_input = validate_time()

    start_datetime = datetime.datetime.strptime(
        f"{date_input} {start_time_input}", "%Y-%m-%d %H:%M")
    end_datetime = start_datetime + datetime.timedelta(minutes=30)

    start_datetime_str = start_datetime.strftime("%Y-%m-%dT%H:%M:%S")
    end_datetime_str = end_datetime.strftime("%Y-%m-%dT%H:%M:%S")

    location = get_location()
    email_notification = email_notification_validation()
    popup_notification = pop_up_notification_validation()
    recurring, recurrence = recurring_event_validation()
    notes = notes_validation()

    full_name = f"{name} {surname}"
    return full_name, start_datetime_str, end_datetime_str, location, volunteer_topic, email_notification, popup_notification, recurring, recurrence, notes


def print_event_details(event):
    clear_terminal()
    if event:
        table = PrettyTable(["\033[92mAttribute\033[0m",
                            "\033[92mValue\033[0m"])
        table.align["Attribute"] = "l"
        table.align["Value"] = "l"

        table.add_row(["\033[91mEvent ID\033[0m",
                      "\033[93m" + event['id'] + "\033[0m"])
        table.add_row(["\033[91mSummary\033[0m", "\033[93m" +
                      event['summary'] + "\033[0m"])
        table.add_row(["\033[91mDescription\033[0m",
                      "\033[93m" + event['description'] + "\033[0m"])

        start_time = datetime.datetime.fromisoformat(
            event['start']['dateTime'])
        formatted_start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        table.add_row(["\033[91mStart Time\033[0m",
                      "\033[93m" + formatted_start_time + "\033[0m"])

        end_time = datetime.datetime.fromisoformat(event['end']['dateTime'])
        formatted_end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        table.add_row(["\033[91mEnd Time\033[0m", "\033[93m" +
                      formatted_end_time + "\033[0m"])

        table.add_row(["\033[91mLocation\033[0m", "\033[93m" +
                      event.get('location', 'Not specified') + "\033[0m"])

        if 'recurrence' in event:
            recurrence = 'Yes'
            recurrence_type = event['recurrence'][0].split('=')[1]
        else:
            recurrence = 'No'
            recurrence_type = 'Not applicable'

        table.add_row(["\033[91mRecurring\033[0m",
                      "\033[93m" + recurrence + "\033[0m"])
        table.add_row(["\033[91mRecurring Type\033[0m",
                      "\033[93m" + recurrence_type + "\033[0m"])

        if event.get('reminders', {}).get('useDefault', False):
            notification = 'Yes'
        else:
            notification = 'No'

        table.add_row(["\033[91mNotification\033[0m",
                      "\033[93m" + notification + "\033[0m"])

        print("Event Details:")
        print(table)


def main():
    print_fancy_message("WELCOME TO OUR VOLUNTEER SYSTEM: CREATE A SLOT")
    volunteer_name, start_datetime, end_datetime, location, volunteer_topic, email_notification, popup_notification, recurring, recurrence, notes = get_user_input_full()

    book_slot(volunteer_name, start_datetime, end_datetime, location, volunteer_topic,
              email_notification, popup_notification, recurring, recurrence, notes)


if __name__ == "__main__":
    main()
