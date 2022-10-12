"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""


# Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)
