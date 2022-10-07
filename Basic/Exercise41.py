"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 16
       CSE, 2018, HSTU
"""

# Calculate the cube of all numbers from 1 to a given number

number = int(input("Enter your number : "))

for i in range(1, number+1):
    print(f"Current number is {i}, and cube is {i**3}")
