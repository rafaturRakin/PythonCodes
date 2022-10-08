"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""


# Write a program to create function calculation() such that it can accept two variables and
# calculate addition and subtraction.  Also, it must return both addition and subtraction in a single return call.
def calculation(a, b):
    return a + b, a - b


print(calculation(5, 10))
