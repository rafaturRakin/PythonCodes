"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 14
       CSE, 2018, HSTU
"""

# Reverse a given integer number
number = int(input("Enter your number : "))

reversedNumber = 0
x = number

while x:
    reversedNumber = (reversedNumber * 10) + (x % 10)
    x = x // 10

print(f"Actual number : {number}, Reverse number : {reversedNumber}")
