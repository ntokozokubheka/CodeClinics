import json
from prettytable import PrettyTable
import textwrap
from datetime import datetime
from src.helpers.utils import clear_terminal
from src.authentification.encryption import read_email_from_file


def wrap_text(text, width):
    return '\n'.join(textwrap.wrap(text, width=width))


def extract_topic(description):
    parts = description.split('topic covered')
    if len(parts) > 1:
        return parts[1].strip().split('.')[0]
    else:
        return ""


def color_red(text):
    return f"\033[91m{text}\033[0m"


def color_green(text):
    return f"\033[92m{text}\033[0m"


def display_filtered_events(file_path, filter_type):
    clear_terminal()
    filter_email = read_email_from_file(".session.txt")
    try:
        with open(file_path, 'r') as file:
            events = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    table = PrettyTable()
    table.field_names = [color_red("Topic"), color_red("Location"), color_red(
        "Start Time"), color_red("Organizer Email"), color_green("Number of Attendees")]
    table.max_width = 120
    table.padding_width = 1

    for event in events:
        if filter_type == "organizer":
            email_list = [event["organizer"]["email"]]
        elif filter_type == "attendee":
            email_list = [attendee["email"]
                          for attendee in event.get("attendees", [])]
        else:
            print("Invalid filter type.")
            return

        if filter_email in email_list:
            location = event.get("location", "")
            description = event.get("description", "")
            topic = extract_topic(description)
            start_time = event["start"]["dateTime"]
            start_time_formatted = datetime.fromisoformat(
                start_time).strftime('%Y-%m-%d %H:%M')
            organizer_email = event["organizer"]["email"]
            num_attendees = len(event.get("attendees", []))
            table.add_row([color_red(topic), color_red(location), color_red(
                start_time_formatted), color_red(organizer_email), color_green(num_attendees)])

    print(table)
