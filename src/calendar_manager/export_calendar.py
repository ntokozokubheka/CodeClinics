import json
from icalendar import Calendar, Event
from datetime import datetime
import os
from src.helpers.utils import print_yellow, print_green, print_red

def load_calendar_from_json(file_path):
    """
    Load calendar information from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing calendar data.

    Returns:
        list: A list of dictionaries representing calendar events.
    """
    with open(file_path, 'r') as file:
        calendar_data = json.load(file)
    return calendar_data

def export_to_ical(calendar_data, output_dir):
    """
    Export calendar data to iCal format.

    Args:
        calendar_data (list): A list of dictionaries representing calendar events.
        output_dir (str): The path to the output directory.
    """
    cal = Calendar()

    for event_data in calendar_data:
        event = Event()
        event.add('summary', event_data['summary'])
        event.add('description', event_data.get('description', ''))

        start_time = datetime.fromisoformat(
            event_data['start']['dateTime'][:-6])
        end_time = datetime.fromisoformat(event_data['end']['dateTime'][:-6])

        event.add('dtstart', start_time)
        event.add('dtend', end_time)

        location = event_data.get('location', '')
        if location:
            event.add('location', location)

        cal.add_component(event)

    output_file = os.path.join(output_dir, 'calendar.ics')
    with open(output_file, 'wb') as file:
        file.write(cal.to_ical())

def main():
    """
    Main function to load calendar data from JSON and export it to iCal format.
    """
    calendar_data = load_calendar_from_json('data/coding_clinic_calendar.json')
    output_dir = 'data' 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    export_to_ical(calendar_data, output_dir)
    print_green("iCal file generated successfully.")
