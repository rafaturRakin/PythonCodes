"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""


# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def recursive_sum(num):
    if num == 0:
        return 0
    return recursive_sum(num - 1) + num


print(recursive_sum(120))
