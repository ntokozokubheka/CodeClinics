import shutil
from src.helpers.utils import clear_terminal, print_yellow
import time


def display_welcome_message():
    """Display the welcome message with a typing effect in green."""
    message = """
    
\033[92m██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░░░░░░░██╗░░░██╗░██████╗███████╗██████╗░
██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗░░░░░░██║░░░██║██╔════╝██╔════╝██╔══██╗
███████║█████╗░░██║░░░░░██║░░░░░██║░░██║█████╗██║░░░██║╚█████╗░█████╗░░██████╔╝
██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║╚════╝██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
██║░░██║███████╗███████╗███████╗╚█████╔╝░░░░░░╚██████╔╝██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░░░░░░░░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
                                                              
Ｗｅｌｃｏｍｅ ｔｏ ｔｈｅ Ｃｏｄｅ Ｃｌｉｎｉｃｓ Ｂｏｏｋｉｎｇ Ｓｙｓｔｅｍ！               
    Ｈｏｗ ｃａｎ ｗｅ ａｓｓｉｓｔ ｙｏｕ ｔｏｄａｙ？
______________________________________________________________________________________​​​​​​\033[0m"""

    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.025)

    print_help()


def print_fancy_line(color_code="\033[36m"):
    """
    Prints a colored line covering the entire terminal width with a default delay
    """
    delay = 0.025
    terminal_width = shutil.get_terminal_size().columns
    colored_line = color_code + "_" * terminal_width + "\033[0m"
    for char in colored_line:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_fancy_message(message, line_color="\033[36m", message_color="\033[35m"):
    """
    Prints a message with colored lines above and below with a default delay
    """
    clear_terminal()
    delay = 0.025
    terminal_width = shutil.get_terminal_size().columns
    print_fancy_line(line_color)
    message_length = len(message)
    padding_length = (terminal_width - message_length) // 2
    padding = " " * padding_length
    colored_message = message_color + message + "\033[0m"
    print(padding + "\n" + colored_message)
    print_fancy_line(line_color)
    print()


def print_help():
    print("\033[93m")  
    print("""
    \033[92mThis system allows students to:
    - Book appointments
    - View calendars
    - Cancel bookings
    - Volunteer for time slots
    - Cancel volunteering

    For detailed commands, type:

    ./cc help
   
    *** Note: Pay close attention to the grammar on the commands. ***
    """)
    print("\033[0m")