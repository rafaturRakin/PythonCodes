"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 11
       CSE, 2018, HSTU
"""


# Write a Program to extract each digit from an integer in the reverse order.
def extract_digit(number):
    while number:
        print(number % 10, end=' ')
        number = number // 10
    print()


extract_digit(7536)
