"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 16
       CSE, 2018, HSTU
"""


# Removal all characters from a string except integers

string = 'I am 25 years and 10 months old'

new_string = "".join([item for item in string if item.isdigit()])

print(f"New string is {new_string}")
