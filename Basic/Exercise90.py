"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 09
       CSE, 2018, HSTU
"""


# You have given a Python list. Write a program to find value 20 in the list,
# and if it is present, replace it with 200.
# Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]

list1[list1.index(20)] = 200

print(list1)