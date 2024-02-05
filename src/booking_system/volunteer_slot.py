import json
import os.path
from datetime import datetime
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


def book_slot(volunteer_name, slot_datetime):
    # Load volunteer data from file
    with open("data/volunteers.json", "r") as file:
        volunteers = json.load(file)

    if slot_datetime not in volunteers["slots"]:

        volunteers["slots"][slot_datetime] = volunteer_name

        with open("data/volunteers.json", "w") as file:
            json.dump(volunteers, file, indent=4)

        update_google_calendar(volunteer_name, slot_datetime)

        print(f"Slot booked for {volunteer_name} at {slot_datetime}.")
    else:
        print("Slot is already booked. Please choose another slot.")


def update_google_calendar(volunteer_name, slot_datetime):
   
    creds = None
    if os.path.exists("config/.token.json"):
        creds = Credentials.from_authorized_user_file("config/.token.json")

  
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Implement the OAuth flow to get the credentials
            # This could be similar to the flow in your main function
            pass

    service = build("calendar", "v3", credentials=creds)

    event = {
        'summary': 'Coding Clinic Volunteer Slot',
        'description': f'Volunteering for coding clinic by {volunteer_name}',
        'start': {
            'dateTime': slot_datetime,
            'timeZone': 'Your_Time_Zone',
        },
        'end': {
            'dateTime': slot_datetime,
            'timeZone': 'Your_Time_Zone',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")


# Example usage
if __name__ == "__main__":
    volunteer_name = "John Doe"
    slot_datetime = "2024-01-28T10:00:00"

    try:
        datetime.strptime(slot_datetime, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print("Invalid datetime format. Please use YYYY-MM-DDTHH:MM:SS format.")
        exit()

    book_slot(volunteer_name, slot_datetime)