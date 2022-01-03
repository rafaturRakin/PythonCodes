"""
Author: Rakin
Date: 03-01-2021
Language: Python
Topic: Profile a python script
"""

import cProfile


def my_function():
    print("This is a demo function")


if __name__ == '__main__':
    cProfile.run('my_function()')
