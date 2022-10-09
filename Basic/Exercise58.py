"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""


# Count all letters, digits, and special symbols from a given string
def count_characters(string):
    letters = digits = special = 0
    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1

    print(f"Total digits = {digits}\nTotal letters = {letters}\nTotal special character = {special}")


count_characters("P@#yn26at^&i5ve")