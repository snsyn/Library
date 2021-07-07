import sys
import os


# CLI cleaner
def cli_cleaner():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')
