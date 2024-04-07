import json
from datetime import datetime, timedelta  # Update import statement
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from src.helpers.utils import print_yellow, print_green, print_red
from src.helpers.display_graphics import print_fancy_message


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CLIENT_SECRET_FILE = 'data/credentials.json'
CALENDAR_DATA_FILE = 'data/coding_clinic_calendar.json'


def fetch_calendar_events(start_date, end_date):
    """
    Fetches events from the user's primary Google Calendar within the specified date range.

    Args:
        start_date (str): The start date in YYYY-MM-DD format.
        end_date (str): The end date in YYYY-MM-DD format.

    Returns:
        list: A list of dictionaries representing calendar events.
    """
    creds = None
    token_file_path = os.path.expanduser('~/.token.json')

    if os.path.exists(token_file_path):
        creds = Credentials.from_authorized_user_file(token_file_path)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_file_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    start_date = datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
    end_date = (datetime.strptime(end_date, '%Y-%m-%d') +
                timedelta(days=1)).isoformat() + 'Z'

    events = service.events().list(calendarId='primary',
                                   timeMin=start_date, timeMax=end_date,
                                   singleEvents=True,
                                   orderBy='startTime').execute().get('items', [])

    return events


def save_data_to_file(data):
    """
    Saves calendar data to a JSON file.

    Args:
        data (list): A list of dictionaries representing calendar events.
    """
    with open(CALENDAR_DATA_FILE, 'w') as file:
        json.dump(data, file)


def update_next_seven_days():
    """
    Function to update events in the next 7 days.
    """

    today = datetime.today().date()
    start_date = today.strftime("%Y-%m-%d")
    end_date = (today + timedelta(days=7)).strftime("%Y-%m-%d")

    calendar_data = fetch_calendar_events(start_date, end_date)
    save_data_to_file(calendar_data)
    print_green("Events for the next 7 days have been updated successfully.")


def personal_update():
    """
    Function for personal update.
    """
    start_date = input("\033[94mEnter the start date (YYYY-MM-DD): \033[0m")
    end_date = input("\033[94mEnter the end date (YYYY-MM-DD): \033[0m")

    calendar_data = fetch_calendar_events(start_date, end_date)
    save_data_to_file(calendar_data)
    print_green("Personal update has been completed successfully.")


def main():
    """
    Main function to choose between updating events in the next 7 days or a personal update.
    """
    print_fancy_message(
        "WELCOME TO OUR CALENDER MANAGEMENT SYSTEM: UPDATE CALENDAR DATA")
    print_yellow("\n1. Update events in the next 7 days")
    print_yellow("2. Personal update")

    choice = input("\033[94mEnter your choice (1 or 2): \033[0m")

    if choice == '1':
        update_next_seven_days()
    elif choice == '2':
        personal_update()
    else:
        print_red("Invalid choice. Please enter 1 or 2.")