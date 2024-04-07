from src.helpers.utils import print_red


def email_notification_validation():
    email_notification = input(
        "\033[94mDo you want to receive email notifications? (y/n): \033[0m").lower()
    if email_notification == 'y':
        return True
    elif email_notification == 'n':
        return False
    else:
        print_red("Invalid input. Please enter 'y' or 'n'.")
        return email_notification_validation()


def pop_up_notification_validation():
    pop_up_notification = None
    while pop_up_notification not in ['y', 'n']:
        pop_up_notification = input(
            "\033[94mDo you want to receive pop up notifications? (y/n): \033[0m").lower()
        if pop_up_notification == 'y':
            return True
        elif pop_up_notification == 'n':
            return False
        else:
            print_red("Invalid input. Please enter 'y' or 'n'.")


def recurring_event_validation():
    recurring = input(
        "\033[94mDo you want this event to recur? (y/n): \033[0m").lower()

    if recurring == 'y':
        while True:
            recurrence = input("Enter the recurrence pattern "
                               "(e.g., daily, weekly, monthly): ").lower()
            if recurrence in ['daily', 'weekly', 'monthly']:
                return recurring, recurrence
            else:
                print_red(
                    "Invalid recurrence pattern. Please enter 'daily', 'weekly', or 'monthly'.")

    elif recurring == 'n':
        return None, None
    else:
        print_red("Invalid input. Please enter 'y' or 'n'.")
        return recurring_event_validation()


def notes_validation():
    want_notes = input(
        "\033[94mDo you want to enter notes? (y/n): \033[0m").lower()

    if want_notes == 'y':
        notes = input(
            "\033[94mEnter any notes or comments for the appointment or event: \033[0m")
        return notes
    elif want_notes == 'n':
        return None
    else:
        print_red("Invalid input. Please enter 'y' or 'n'.")
        return notes_validation()