"""
#Author     : Rakin
#Date       : 05-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 04
       CSE, 2018, HSTU
"""


# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(string, length):
    return string[length:]


print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
