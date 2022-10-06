"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 10
       CSE, 2018, HSTU
"""


# Given a two list of numbers, write a program to create a new list such that
# the new list should contain odd numbers from the first list and even numbers from the second list.
def create_list(list1, list2):
    new_list = [x for x in list1 if x % 2 == 1] + [x for x in list2 if x % 2 == 0]
    print("result list is : ", new_list)


create_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])
