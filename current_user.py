"""
Author: Rakin
Date: 03-01-2021
Language: Python
Topic: Current username of the system
"""

import getpass
if __name__ == '__main__':
    print(f"Current user is {getpass.getuser()}")
