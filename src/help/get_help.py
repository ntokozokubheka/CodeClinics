from src.helpers.utils import clear_terminal

def print_help():
    clear_terminal()
    print("""\033[92m *** Note: These are the available commands in Code Clinic. ***

\t\033[6m Code Clinic Commands

    help                displays the description of each command.   
    sign_up             registers a new user.
    sign_in             logs the user into the system.
    configure_system    creates the user token.
    verify              verifies whether the connection to Google calender was successful.
    calendar            displays the calender.
    calendar jhb_main   displays the johannesburg main campus calender.
    calendar jhb_cjc   displays the johannesburg cjc campus calender.
    calendar dbn        displays the durban campus calender.
    calendar cpt        displays the cape town campus calender.
    calendar online     displays the calender with slots scheduled online.
    update_calendar     updates the data file of the calendar.
    volunteer_slot      volunteer for a time slot.
    book_slot           book an available time slot.
    export_calendar     exports the users booking to ical format.
    cancel_booking      enables the student to remove themselves from a booking.
    cancel_volunteer    enables the volunteer to remove the event from the calendar.
    volunteered_slots   displays the slots  that you have volunteered for.
    booked_slots        displays the booking you have made on available slots.
    sign_out            logs the user out of the system.
    

 Use the instruction provided above where [command], is one of the CODE CLINICS commands.
 *Note: do not include the square brackets.

 \tEXAMPLE: \33[100m. python3 main.py calendar\033[0m""")