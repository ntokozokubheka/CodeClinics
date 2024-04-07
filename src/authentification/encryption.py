import base64
import os
from cryptography.fernet import Fernet
from src.helpers.common_constants import KEY_FILE
from src.helpers.utils import print_red ,print_green


def load_key_from_file():
    """
    Load the encryption key from the key file.
    """
    try:
        with open(KEY_FILE, "rb") as f:
            return f.read()
    except Exception as e:
        print_red(f"Error loading encryption key: {str(e)}")
        return None


def save_key_to_file(key):
    """
    Save the encryption key to the key file.
    """
    try:
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    except Exception as e:
        print_red(f"Error saving encryption key: {str(e)}")


def generate_key():
    """
    Generate a new encryption key.
    """
    return Fernet.generate_key()


def encrypt_value(value):
    """
    Encrypt a value using the encryption key and return as a string.
    """
    key = load_key_from_file()
    if key:
        try:
            f = Fernet(key)
            encrypted_value = f.encrypt(value.encode())

            encrypted_value_str = base64.urlsafe_b64encode(
                encrypted_value).decode()
            return encrypted_value_str
        except Exception as e:
            print_red(f"Encryption error: {str(e)}")
            return None
    else:
        print_red("Encryption key not loaded.")
        return None


def decrypt_value(encrypted_value_str):
    """
    Decrypt an encrypted value string using the key loaded from the file.
    """
    key = load_key_from_file()
    if key:
        try:
            f = Fernet(key)

            encrypted_value = base64.urlsafe_b64decode(
                encrypted_value_str.encode())
            decrypted_value = f.decrypt(encrypted_value).decode()
            return decrypted_value
        except Exception as e:
            print_red(f"Decryption error: {str(e)}")
            return None
    else:
        print_red("Encryption key not loaded.")
        return None


def read_email_from_file(file_name):
    """
    Read email from a text file.

    Args:
        file_name (str): Name of the text file containing the email.

    Returns:
        str: Email read from the file.
    """

    home_directory = os.path.expanduser('~')
    file_path = os.path.join(home_directory, file_name)

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            if lines:
                email = lines[0].strip()

                return decrypt_value(email)
            else:
                print_green(f"File {file_path} is empty.")
                return None
    except FileNotFoundError:
        print_red(f"File {file_path} not found.")
        return None
