import json
from config.quick_start import main


def update_calender_data():

    # Fetch new events
    new_events = main()

    # Load existing events from file if it exists
    try:
        with open("data/coding_clinic_calendar.json", "r") as json_file:
            existing_events = json.load(json_file)
    except FileNotFoundError:
        existing_events = None

    # Compare new events with existing events
    if new_events != existing_events:
        # If the data is different, update the file
        with open("data/coding_clinic_calendar.json", "w") as json_file:
            json.dump(new_events, json_file, indent=4)
        print("Calendar data updated successfully.")
    else:
        print("Calendar data is already up to date.")


if __name__ == "__main__":

    update_calender_data()
