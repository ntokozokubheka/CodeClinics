import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from src.authentification.encryption import read_email_from_file
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from src.helpers.common_constants import CALENDAR_ID, SCOPES, TOKEN_FILE, CLIENT_SECRET_FILE
from src.helpers.utils import print_red


def validate_calendar_account(creds):
    stored_email = read_email_from_file(".session.txt")

    if not stored_email:
        raise ValueError("Email not found or invalid.")

    if not creds:
        raise ValueError("Failed to retrieve credentials.")

    user_email = get_user_email(creds)
    if not user_email:
        raise ValueError("Failed to retrieve user email.")

    if user_email != stored_email:
        raise ValueError("Email does not match.")

    return user_email


def get_google_credentials():
    """
    Retrieve credentials from token file or perform OAuth flow.

    Returns:
        Credentials: The OAuth2 credentials.
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE,
                scopes=SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def get_user_email(creds):
    """
        This function checks if the users email is a wethinkcode email address.
        :param creds: the users google calendar creds.
        :return True, user_email: if the email is valid.
        :return False, "": if the  email is not valid.
    """
    service = build('calendar', 'v3', credentials=creds)
    results = service.calendarList().get(calendarId="primary").execute()
    return results["id"]
