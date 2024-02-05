import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
from datetime import datetime

def cancel_booking(volunteer_name, slot_datetime):
    # Load volunteer data from file
    with open("data/volunteers.json", "r") as file:
        volunteers = json.load(file)

    if volunteers["slots"].get(slot_datetime) == volunteer_name:
        # Remove the event from the volunteer's Google Calendar
        remove_google_calendar_event(slot_datetime)

        # Mark the slot as available again
        del volunteers["slots"][slot_datetime]

        # Update data file
        with open("data/volunteers.json", "w") as file:
            json.dump(volunteers, file, indent=4)

        print(f"Booking canceled for {volunteer_name} at {slot_datetime}.")
    else:
        print(f"No booking found for {volunteer_name} at {slot_datetime}.")

# Function to remove event from volunteer's Google Calendar
def remove_google_calendar_event(slot_datetime):
    
    creds = None
    if os.path.exists("config/.token.json"):
        creds = Credentials.from_authorized_user_file("config/.token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
          
            creds = get_google_credentials()

    service = build("calendar", "v3", credentials=creds)

    calendar_id = 'primary'

    try:
        
        events_result = service.events().list(calendarId=calendar_id, timeMin=slot_datetime, timeMax=slot_datetime, singleEvents=True).execute()
        events = events_result.get('items', [])

        if events:
            event_id = events[0]['id']
            service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
            print(f"Event at {slot_datetime} deleted successfully.")
        else:
            print(f"No event found at {slot_datetime}.")
    except Exception as e:
        print(f"An error occurred while deleting the event: {str(e)}")

# Function to perform OAuth flow and get credentials
def get_google_credentials():
   
   
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file(
        'path_to_client_secret_file.json', scopes=SCOPES)

    credentials = flow.run_local_server(port=0)

    return credentials

# Example usage
if __name__ == "__main__":
    volunteer_name = "John Doe"
    slot_datetime = "2024-01-28T10:00:00"  

    try:
        datetime.strptime(slot_datetime, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print("Invalid datetime format. Please use YYYY-MM-DDTHH:MM:SS format.")
        exit()

    cancel_booking(volunteer_name, slot_datetime)
