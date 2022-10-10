"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 13
       CSE, 2018, HSTU
"""


# Split a string on hyphens
string = "Emma-is-a-data-scientist"

print("Printing each substring: ")
for substring in string.split('-'):
    print("\t" + substring)
