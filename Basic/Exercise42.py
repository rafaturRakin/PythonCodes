"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 17
       CSE, 2018, HSTU
"""

# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

number = int(input("Enter your number : "))

start = 2
currentNumber = 0

for i in range(number):
    print(start, end=' + ')
    currentNumber += start
    start = (start * 10) + 2

print("\nResult is :", currentNumber)
