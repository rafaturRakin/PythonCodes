"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""

# Count the total number of digits in a number
number = int(input("Enter the number: "))
digits = 0

while number:
    digits += 1
    number //= 10

print(digits)
