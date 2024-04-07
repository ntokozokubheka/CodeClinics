import re
from datetime import datetime, timedelta
from src.helpers.utils import print_red


def validate_single_date():
    try:
        date_string = input("\033[94mEnter date (YYYY-MM-DD): \033[0m")
        datetime.strptime(date_string, "%Y-%m-%d")
        if is_regular_day(date_string):
            return date_string
        else:

            return validate_single_date()
    except ValueError:
        print_red("Invalid date format. Please enter a valid date.")
        return validate_single_date()


def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_start_date_before_end_date(start_date_str, end_date_str):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        return start_date <= end_date
    except ValueError:
        return False


def process_date():
    start_date = input("\033[94mEnter start date (YYYY-MM-DD): \033[0m")

    while not validate_date_format(start_date):
        print_red("Incorrect date format! Please enter the start date again.")
        start_date = input("\033[94mEnter start date (YYYY-MM-DD): \033[0m")

    end_date = input("\033[94mEnter end date (YYYY-MM-DD): \033[0m")
    while not validate_date_format(end_date):
        print_red("Incorrect date format! Please enter the end date again.")
        end_date = input("\033[94mEnter end date (YYYY-MM-DD): \033[0m")

    while not is_start_date_before_end_date(start_date, end_date):
        print_red("Start date must be before end date!")
        start_date = input("\033[94mEnter start date (YYYY-MM-DD): \033[0m")
        while not validate_date_format(start_date):
            print_red("Incorrect date format! Please enter the start date again.")
            start_date = input(
                "\033[94mEnter start date (YYYY-MM-DD): \033[0m")

        end_date = input("\033[94mEnter end date (YYYY-MM-DD): \033[0m")
        while not validate_date_format(end_date):
            print_red("Incorrect date format! Please enter the end date again.")
            end_date = input("\033[94mEnter end date (YYYY-MM-DD): \033[0m")

    if not is_regular_day(start_date) or not is_regular_day(end_date):
        process_date()

    return start_date, end_date


def validate_time():

    time_pattern = re.compile(r'^([01][0-9]|2[0-3]):([0-5][0-9])$')
    start_time_input = input(
        "\033[94mEnter the slot start time (HH:MM): \033[0m")

    if time_pattern.match(start_time_input):
        if validate_work_hours(start_time_input):
            return start_time_input

    return validate_time()


def validate_work_hours(time_str):
    try:
        hours, minutes = map(int, time_str.split(':'))
        if 7 <= hours < 17 or (hours == 17 and minutes == 0):
            return True
        print_red("Invalid work hours: Session must be between 07:00 to 17:00")
        return False
    except ValueError:
        print_red("Invalid time format. Please use HH:MM format.")
        return False


def is_sunday(date_string):
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        if date_object.weekday() == 6:
            print_red("Bookings not on work days (Mon to Sat) are not allowed")
            return True
        return False
    except ValueError:
        return False


def is_sa_public_holiday(date_string):
    sa_holidays = {
        "01-01": "New Year's Day",
        "03-21": "Human Rights Day",
        "04-19": "Good Friday",
        "04-22": "Family Day",
        "04-27": "Freedom Day",
        "05-01": "Workers' Day",
        "06-16": "Youth Day",
        "08-09": "National Women's Day",
        "09-24": "Heritage Day",
        "12-16": "Day of Reconciliation",
        "12-25": "Christmas Day",
        "12-26": "Day of Goodwill",
    }

    month_day = date_string[5:]

    if month_day in sa_holidays:
        print_red(
            f"{sa_holidays[month_day]}: Bookings on holidays are not allowed")
        return True
    else:
        return False


def get_johannesburg_date():
    try:
        johannesburg_date = datetime.now().date()
        return johannesburg_date
    except Exception as e:
        print_red(f"Error occurred while fetching Johannesburg date: {e}")
        return None


def is_regular_day(date_string):
    return not (is_sunday(date_string) or is_sa_public_holiday(date_string))