import os

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/calendar.events']

CLIENT_SECRET_FILE = 'data/credentials.json'

TOKEN_FILE = os.path.expanduser("~/.token.json")


KEY_FILE = os.path.expanduser("~/.encryption_key.txt")

Calender_Timezone = 'Africa/Johannesburg'
CALENDAR_ID = "c_cbaa9da597b10a5784f3eb622af3230ea534be93ca34f77b175ef0a411c1a7d1@group.calendar.google.com"

CALENDAR_DATA_FILE = os.path.join('data', 'coding_clinic_calendar.json')