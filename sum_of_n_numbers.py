"""
Author: Rakin
Date: 01-01-2021
Language: Python
Topic: Sum on N numbers
"""

if __name__ == '__main__':
    number = int(input("Enter the number : "))
    total = int(number * (number + 1) / 2)
    print(f"The sum of first {number} is = {total}")
