from src.helpers import import_helper
from src.authentification import session_control
import sys
from src.helpers.utils import print_red
from src.helpers.common_constants import CALENDAR_DATA_FILE


def manage_authentication():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if (arg == 'sign_in' or arg == 'sign_up'):
            if not session_control.check_user_session()[0]:
                try:
                    user_auth = import_helper.dynamic_import(
                        "src.authentification.user")
                    if arg == 'sign_up':
                        user_auth.sign_up()
                    if arg == 'sign_in':
                        user_auth.sign_in()
                except ImportError:
                    print_red("Error: Could not import module authentication")
            else:
                print_red("User already signed in ,Please sign out first")


def manage_student():
    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'book_slot':
            make_a_booking()

        if arg == 'cancel_booking':
            cancel_a_booking()


def manage_volunteer():
    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'volunteer_slot':
            volunteer_a_slot()

        if arg == 'cancel_volunteer':
            cancel_volunteer_slot()


def manage_calendar():
    view_calendar()
    update_calendar()
    export_calendar()
    view_my_bookings()


def export_calendar():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'export_calendar':
            try:
                export_calendar = import_helper.dynamic_import(
                    "src.calendar_manager.export_calendar")
                export_calendar.main()
            except ImportError:
                print_red("Error: Could not import module 'export_calendar'")


def update_calendar():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == 'update_calendar':
            try:
                calendar = import_helper.dynamic_import(
                    "src.calendar_manager.update_calendar")
                calendar.main()
            except ImportError:
                print_red("Error: Could not import module 'update_calendar'")


def check_configured_connection():
    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'verify':
            try:

                config = import_helper.dynamic_import(
                    "config.quick_start")

                config.check_config_connection()

            except ImportError:

                print_red(f"Error: Could not import config module")


def configure_connection():
    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'configure_system':
            try:

                config = import_helper.dynamic_import(
                    "config.quick_start")

                config.config_main()

            except ImportError:

                print_red(f"Error: Could not import config module")


def help_menu():

    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'help':
            try:
                help_module = import_helper.dynamic_import(
                    "src.help.get_help")
                help_module.print_help()
            except:
                print_red(f"Error: Could not import module help")


def volunteer_a_slot():

    try:

        book_slot = import_helper.dynamic_import(
            "src.booking_system.volunteer_slot")

        book_slot.main()

    except ImportError:

        print_red(f"Error: Could not import module volunteer a slot module")


def cancel_volunteer_slot():

    try:

        book_slot = import_helper.dynamic_import(
            "src.booking_system.cancel_volunteer")

        book_slot.main()

    except ImportError:

        print_red(f"Error: Could not import module cancel volunteer slot")


def cancel_a_booking():

    try:

        book_slot = import_helper.dynamic_import(
            "src.booking_system.cancel_booking")

        book_slot.cancel_booking()

    except ImportError:

        print_red(f"Error: Could not import module cancel volunteer slot")


def make_a_booking():

    try:

        book_slot = import_helper.dynamic_import(
            "src.booking_system.make_booking")

        book_slot.main()

    except ImportError:

        print_red(f"Error: Could not import module make booking")


def sign_out_session():

    if len(sys.argv) > 1:

        arg = sys.argv[1]
        if arg == 'sign_out':
            session_control.sign_out()


def view_calendar():

    if len(sys.argv) > 1:

        arg = sys.argv[1]

        if arg == 'calendar' and len(sys.argv) == 2:
            try:
                calendar = import_helper.dynamic_import(
                    "src.calendar_manager.view_calendar")
                calendar.view_calendar()
            except:
                print_red(f"Error: Could not import module view calendar")

        if len(sys.argv) > 2:
            arg_two = sys.argv[2]

            if arg_two == 'jhb_cjc':
                try:
                    calendar = import_helper.dynamic_import(
                        "src.calendar_manager.view_campus_schedules")
                    calendar.display_filtered_events(
                        CALENDAR_DATA_FILE, "jhb cjc")
                except:
                    print_red(
                        f"Error: Could not import module view campus schedule")
            if arg_two == 'jhb_main':
                try:
                    calendar = import_helper.dynamic_import(
                        "src.calendar_manager.view_campus_schedules")
                    calendar.display_filtered_events(
                        CALENDAR_DATA_FILE, "jhb main")
                except:
                    print_red(
                        f"Error: Could not import module view campus schedule")
            if arg_two == 'dbn':
                try:
                    calendar = import_helper.dynamic_import(
                        "src.calendar_manager.view_campus_schedules")
                    calendar.display_filtered_events(CALENDAR_DATA_FILE, "dbn")
                except:
                    print_red(
                        f"Error: Could not import module view campus schedule")

            if arg_two == 'cpt':
                try:
                    calendar = import_helper.dynamic_import(
                        "src.calendar_manager.view_campus_schedules")
                    calendar.display_filtered_events(CALENDAR_DATA_FILE, "cpt")
                except:
                    print_red(
                        f"Error: Could not import module view campus schedule")
            if arg_two == 'online':
                try:
                    calendar = import_helper.dynamic_import(
                        "src.calendar_manager.view_campus_schedules")
                    calendar.display_filtered_events(
                        CALENDAR_DATA_FILE, "online")
                except:
                    print_red(
                        f"Error: Could not import module view campus schedule")


def view_my_bookings():
    if len(sys.argv) > 2:
        arg_two = sys.argv[2]

        if arg_two == 'volunteered_slots':
            try:
                calendar = import_helper.dynamic_import(
                    "src.calendar_manager.view_my_bookings")
                calendar.display_filtered_events(
                    CALENDAR_DATA_FILE, "organizer")
            except ImportError:
                print_red(
                    f"Error: Could not import module view my bookings")
        elif arg_two == 'booked_slots':
            try:
                calendar = import_helper.dynamic_import(
                    "src.calendar_manager.view_my_bookings")
                calendar.display_filtered_events(
                    CALENDAR_DATA_FILE, "attendee")
            except ImportError:
                print_red(
                    f"Error: Could not import module view my bookings")


def main():
    manage_authentication()
    help_menu()

    if len(sys.argv) > 1 and session_control.check_user_session()[0]:
        manage_calendar()
        manage_volunteer()
        manage_student()
        check_configured_connection()
        configure_connection()

        sign_out_session()

    else:

        print_red(
            "\n******************************** Please sign in! ********************************\n")