"""
Author: Rakin
Date: 01-01-2021
Language: Python
Topic: Factorial of a Number
"""

if __name__ == '__main__':
    factorial = 1
    number = int(input("Enter a number : "))

    if number < 0:
        print("Factorial of Negative number is not defined")
    elif number == 0:
        print(f"Factorial of {number} is = {factorial}")
    else:
        for i in range(1, number + 1):
            factorial = factorial * i
        print(f"Factorial of {number} is = {factorial}")
