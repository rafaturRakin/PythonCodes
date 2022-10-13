"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 04
       CSE, 2018, HSTU
"""


# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dictionary = dict()

for item in employees:
    dictionary.setdefault(item, defaults)

print(dictionary)

print("\nMethod #02: fromkeys() ->")
result = dict.fromkeys(employees, defaults)
print(result)
