import os
import re
import getpass
from validate_email import validate_email
from src.authentification.encryption import load_key_from_file, encrypt_value, decrypt_value, generate_key, save_key_to_file
from src.authentification.session_control import save_user_to_file, sign_out
from src.helpers.utils import create_hidden_text_files_in_home
from src.helpers.common_constants import KEY_FILE
from src.helpers.display_graphics import display_welcome_message, print_fancy_message
from src.helpers.utils import print_red, print_yellow, print_green, clear_terminal


def manage_user_file():
    """
    Manages user file operations and key management.
    Returns the file path and the encryption key.
    """
    try:

        home_directory = os.path.expanduser('~')
        file_path = os.path.join(home_directory, ".user_details.txt")

        if os.path.exists(KEY_FILE):
            key = load_key_from_file()
        else:
            key = generate_key_and_save()

        return file_path
    except Exception as e:
        print_red(f"Error in managing user file: {str(e)}")
        return None, None


def generate_key_and_save():
    """
    Generate a new encryption key and save it to the key file.
    """
    try:
        key = generate_key()
        save_key_to_file(key)
        return key
    except Exception as e:
        print_red(f"Error generating and saving encryption key: {str(e)}")
        return None


def sign_up():
    """
    Allows users to sign up by providing their details.
    """
    try:
        create_hidden_text_files_in_home()
        print_fancy_message(
            "WELCOME TO THE USER AUTHENTICATION SYSTEM: SIGN UP")
        print_yellow("Please sign up by providing your details.")
        username = get_username()
        email = get_email()
        password = get_password()

        file_path = manage_user_file()

        if file_path:
            encrypted_username = encrypt_value(username)
            encrypted_email = encrypt_value(email)
            encrypted_password = encrypt_value(password)

            with open(file_path, "a") as file:
                file.write(
                    f"{encrypted_username},{encrypted_email},{encrypted_password}\n")
            print_green("You've successfully registered")
            sign_out()
            print()
            sign_in()
    except Exception as e:
        print_red(f"An error occurred during sign up: {str(e)}")


def sign_in():
    """
    Allows users to sign in.
    """
    try:
        print_fancy_message(
            "WELCOME TO THE USER AUTHENTICATION SYSTEM: SIGN IN")
        print_yellow("Please sign in.")
        email = get_email()
        password = getpass.getpass("Password: ").strip()

        if check_credentials(email, password):
            save_user_to_file(".session.txt", encrypt_value(email))
            clear_terminal()
            print_green("Login successful!")
            display_welcome_message()

        else:
            print_red("Invalid credentials. Please try again.")
    except Exception as e:
        print_red(f"An error occurred during sign in: {str(e)}")


def check_credentials(email, password):
    """
    Validates user credentials.
    """
    try:
        file_path = manage_user_file()

        if file_path:
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        stored_username, stored_email, stored_password = parts
                        decrypted_email = decrypt_value(
                            stored_email)
                        decrypted_password = decrypt_value(
                            stored_password)
                        if email == decrypted_email and password == decrypted_password:
                            return True
                    else:
                        print_red("Invalid data format in user file.")
    except Exception as e:
        print_red(f"Error checking credentials: {str(e)}")
        return False

    return False


def is_user_registered(username):
    """
    Checks if the user is already registered.
    """
    try:
        file_path = manage_user_file()

        if file_path:
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 1:
                        if (not parts):
                            return False
                        stored_username = decrypt_value(parts[0])
                        if username == stored_username:
                            return True
    except Exception as e:
        print_red(f"Error checking if user is registered: {str(e)}")
        return False

    return False


def validate_password(password):
    """
    Validates the password.
    """
    if len(password) < 8:
        print_red("The Password must be at least 8 characters long.")
        return False
    elif not re.search("[a-z]", password):
        print_red("The Password must contain at least one lowercase letter.")
        return False
    elif not re.search("[A-Z]", password):
        print("The Password must contain at least one uppercase letter.")
        return False
    elif not re.search("[0-9]", password):
        print_red("The Password must contain at least one number.")
        return False
    elif not re.search("[!@#$%&?]", password):
        print_red(
            "The password must contain at least one special character. Choose between [!@#$%&?]")
        return False
    else:
        return True


def is_valid_email(email):
    """
    Validates the email format.
    """
    if email.endswith("@student.wethinkcode.co.za") and validate_email(email):
        return True
    else:
        print_red("Invalid email format. Email must be from @")


def get_username():
    while True:
        username = input("\033[94mCreate a Username: \033[0m").strip()
        if not is_user_registered(username):
            return username
        else:
            print_red("This Username already exists. Please try again.")


def get_email():
    while True:
        email = input("\033[94mEnter your email: \033[0m").strip()

        if validate_email(email):
            return email
        else:
            print_red("Invalid email format. Please try again.")


def get_password():
    while True:
        password = getpass.getpass(
            "\033[94mCreate a password: \033[0m").strip()
        if validate_password(password):
            return password
        else:
            print_red("Invalid password format. Please try again.")


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print_red(f"Error: File '{file_name}' not found.")
        return None
    except IOError:
        print_red(f"Error: Could not read from file '{file_name}'.")
        return None


def save_name_to_file(file_name, name):
    try:
        with open(file_name, 'w') as file:
            file.write(name)
        print_red(f"Name '{name}' saved to file '{file_name}' successfully.")
    except IOError:
        print_red(f"Error: Could not write to file '{file_name}'.")
