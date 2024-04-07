import os
import re


def print_green(message):
    print("\033[92m{}\033[0m".format(message))


def print_red(message):
    print("\033[91m{}\033[0m".format(message))


def print_yellow(message):
    print("\033[93m{}\033[0m".format(message))


def validate_name():
    pattern = r'^[A-Z][a-z]+$'
    name = input("\033[94mEnter your name: \033[0m")

    if re.match(pattern, name):
        return name
    else:
        print_red(
            "Invalid name format. Please enter a name starting with an uppercase letter followed by lowercase letters only.")
        return validate_name()


def validate_surname():
    pattern = r'^[A-Z][a-z]+$'
    surname = input("\033[94mEnter your surname: \033[0m")

    if re.match(pattern, surname):
        return surname
    else:
        print_red("Invalid surname format. Please enter a surname starting with an uppercase letter followed by lowercase letters only.")
        return validate_surname()


def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_hidden_text_files_in_home():
    try:
        home_directory = os.path.expanduser('~')

        file1_path = os.path.join(home_directory, '.user_details.txt')
        file2_path = os.path.join(home_directory, '.session.txt')

        if not os.path.exists(file1_path):
            with open(file1_path, 'w'):
                pass

        if not os.path.exists(file2_path):
            with open(file2_path, 'w'):
                pass

    except IOError as e:
        print_red(f"Error: {e}")


def check_alphabets(input1, input2):

    def filter_alpha(input):
        return ''.join(filter(str.isalpha, str(input))).lower()

    str1 = filter_alpha(input1)
    str2 = filter_alpha(input2)

    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
