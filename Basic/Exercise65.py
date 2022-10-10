"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 12
       CSE, 2018, HSTU
"""


# Find the last position of a given substring
string = "Emma is a data scientist who knows Python. Emma works at google."
substring = "Emma"

print(f"Last occurrence of {substring} is: {string.rfind(substring)}")
