"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""


# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position does not matter.

def is_balanced(string1, string2):
    for x in string1:
        if string2.find(x) == -1:
            return False
    else:
        return True


print(is_balanced("vine", "Pynative"))
