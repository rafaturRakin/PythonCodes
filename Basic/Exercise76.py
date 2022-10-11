"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 05
       CSE, 2018, HSTU
"""


# Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
resultSet = set()

for i in range(len(first_list)):
    resultSet.add((first_list[i], second_list[i]))

print("Result is", resultSet)
