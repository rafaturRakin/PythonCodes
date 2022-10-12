"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 10
       CSE, 2018, HSTU
"""


# Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
print("Before removing 20 :", list1)

list1 = [item for item in list1 if item != 20]
print("After removing 20 :", list1)
