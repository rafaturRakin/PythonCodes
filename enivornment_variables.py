"""
Author: Rakin
Date: 03-01-2021
Language: Python
Topic: Getting environment variables
"""

import os
if __name__ == '__main__':
    variables = os.environ
    for variable in variables:
        print(f"{variable} : {variables[variable]}")
