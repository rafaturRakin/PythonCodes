"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 05
       CSE, 2018, HSTU
"""


# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def outer_func(a, b):
    def inner_func(x, y):
        return x + y

    return inner_func(a, b) + 5


print(outer_func(5, 6))
