"""
#Author     : Rakin
#Date       : 04-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 01
       CSE, 2018, HSTU
"""


# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

def sum_or_product(a, b):
    result = a * b
    if result <= 1000:
        return result
    else:
        return a + b


print("The result is ", sum_or_product(20, 30))
print("The result is ", sum_or_product(40, 30))
