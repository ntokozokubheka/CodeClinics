import datetime
from tabulate import tabulate
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from src.helpers.common_functions import get_google_credentials
from src.helpers.common_constants import CALENDAR_ID
from src.helpers.utils import clear_terminal, print_green, print_red


def view_calendar():
    """
    Fetches upcoming events from the user's primary Google Calendar and displays them in a formatted table.

    This function fetches the upcoming events from the user's primary Google Calendar within a one-week time frame
    starting from the current date. It then formats the events into a table and prints them to the console.

    Raises:
        HttpError: An error occurred while fetching events from the Google Calendar API.
    """
    creds = get_google_credentials()
    clear_terminal()
    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = (
            service.events()
            .list(
                calendarId=CALENDAR_ID,
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        data_to_display = []

        start_date = datetime.datetime.utcnow()
        for i in range(7):
            current_date = start_date + datetime.timedelta(days=i)
            current_date_str = current_date.strftime("%Y-%m-%d")

            events_on_date = [
                event
                for event in events
                if event["start"].get("dateTime", event["start"].get("date"))[:10]
                == current_date_str
            ]

            if events_on_date:
                for event in events_on_date:
                    start_time = event["start"].get(
                        "dateTime", event["start"].get("date"))
                    formatted_start_time = datetime.datetime.fromisoformat(
                        start_time).strftime('%Y-%m-%d %H:%M:%S')
                    attendees = len(event.get("attendees", []))
                    description = event.get("description", "")
                    soup = BeautifulSoup(description, 'html.parser')
                    values = [element.get_text()
                              for element in soup.find_all('td')]
                    max_width = 10
                    for value in values:
                        value = value[:max_width] + \
                            "..." if len(value) > max_width else value
                    max_email_length = 20
                    organizer_email = event["organizer"]["email"] if event.get(
                        "organizer") else ""

                    if len(organizer_email) > max_email_length:
                        organizer_email = organizer_email[:max_email_length] + "..."

                    data_to_display.append(
                        [
                            formatted_start_time[:10],
                            formatted_start_time[11:],
                            event["summary"],
                            organizer_email,
                            event.get("location", ""),
                            attendees
                        ]
                    )
            else:
                event_summary = "No Bookings"
                data_to_display.append(
                    [current_date_str, "", event_summary, "", "", ""])

        print_green("Upcoming Events:")
        print(tabulate(data_to_display, headers=[
              "Date", "Time", "Event", "organizer", "location", "Attendees"], tablefmt="fancy_grid"))

    except HttpError as error:
        print_red(f"An error occurred: {error}")
