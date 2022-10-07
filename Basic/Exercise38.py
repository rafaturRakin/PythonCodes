"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 13
       CSE, 2018, HSTU
"""

# Find the factorial of a given number
number = int(input("Enter your number : "))

factorial = 1
for i in range(1, number+1):
    factorial *= i

print(factorial)
