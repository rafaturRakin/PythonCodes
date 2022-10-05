"""
#Author     : Rakin
#Date       : 05-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 02
       CSE, 2018, HSTU
"""

# Write a program to iterate the first 10 numbers and in each iteration,
# print the sum of the current and previous number.

number = 10
current = 0
previous = 0
total = 0

print(f"Printing current and previous number sum in a range({number})")
for x in range(number):
    previous = current
    current = x
    total = current + previous
    print(f"Current Number {current} Previous Number {previous} Sum : {total}")
