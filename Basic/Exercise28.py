"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""

# Calculate the sum of all numbers from 1 to a given number

number = int(input("Enter the last number : "))
result = 0
for i in range(1, number+1):
    result += i
print(f"Sum is: {result}")
