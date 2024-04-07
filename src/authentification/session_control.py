import os
from src.helpers.utils import print_red, print_green, clear_terminal


def read_file(file_name):

    home_directory = os.path.expanduser('~')
    file_path = os.path.join(home_directory, file_name)

    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        else:
            return False
    except IOError:
        print_red(f"Error: Could not read from file '{file_name}'.")
        return False


def save_user_to_file(file_name, name):
    try:

        home_directory = os.path.expanduser('~')
        file_path = os.path.join(home_directory, file_name)

        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass

        with open(file_path, 'w') as file:
            file.write(name)

    except IOError:
        print_red(f"Error: Could not write to file '{file_path}'.")


def sign_out():

    home_directory = os.path.expanduser('~')
    file_path = os.path.join(home_directory, ".session.txt")

    try:
        with open(file_path, 'w'):
            pass
        clear_terminal()
        print_green("Successfully signed out")
    except IOError:
        print_red(f"Error: Could not clear file '{file_path}'.")


def check_user_session():

    home_directory = os.path.expanduser('~')
    file_path = os.path.join(home_directory, ".session.txt")

    username = read_file(file_path)
    if username:
        return True, username

    return False, "No User Found"