"""
#Author     : Rakin
#Date       : 05-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 05
       CSE, 2018, HSTU
"""


# Write a function to return True if the first and last number of a given list is same,
# if numbers are different return False.

def check_list(numbers):
    print(f"Given list: {numbers}")
    print(f"result is {numbers[0] == numbers[-1]}")


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

check_list(numbers_x)
check_list(numbers_y)
