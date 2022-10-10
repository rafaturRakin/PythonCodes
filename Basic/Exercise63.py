"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 10
       CSE, 2018, HSTU
"""


# Write a program to count occurrences of all characters within a string
string = "Apple"
dictionary = {}

for x in string:
    if dictionary.get(x) is None:
        dictionary[x] = 1
    else:
        dictionary[x] += 1

print(dictionary)
