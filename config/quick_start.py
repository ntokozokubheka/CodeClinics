import os
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.helpers.utils import print_green, print_red
from src.helpers.common_functions import get_google_credentials, validate_calendar_account
from src.helpers.common_constants import TOKEN_FILE


def delete_token_file():
    """
    Deletes the token file if it exists.

    This function checks if the token file exists at the path specified
    by the TOKEN_FILE constant. If the file exists, it removes it.

    Returns:
        None
    """
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)


def config_main():
    """
    Main function for configuring Google Calendar credentials.

    This function is responsible for configuring Google Calendar credentials
    by deleting any existing token files, obtaining new credentials, and validating
    the user's calendar account.

    Returns:
        None
    """
    delete_token_file()
    creds = get_google_credentials()
    validate_calendar_account(creds)
    print_green("System was configured successfully")


def check_config_connection():
    """
    Checks the connection to the Google Calendar API.

    This function verifies if the token file exists. If the file exists,
    it attempts to retrieve credentials and establish a connection to the
    Google Calendar API. It prints a success message if the connection is
    successful, otherwise, it prints an error message.

    Returns:
        None
    """
    if os.path.exists(TOKEN_FILE):
        creds = get_google_credentials()
        if creds:
            try:
                service = build("calendar", "v3", credentials=creds)
                print_green("Connection to Google Calendar API successful.")
            except HttpError as error:
                print_red(f"An error occurred: {error}")
                print_red("Not connected to Google Calendar API.")
    else:
        print_red(f"Token file '{TOKEN_FILE}' does not exist.")
        print_red("Not connected to Google Calendar API.")