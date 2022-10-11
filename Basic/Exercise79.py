"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""

# Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

sample_values = list(sample_dict.values())

roll_number = [item for item in roll_number if item in sample_values]

print("After removing unwanted elements from list", roll_number)
