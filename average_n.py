"""
Author: Rakin
Date: 01-01-2021
Language: Python
Topic: Average on N numbers
"""

if __name__ == '__main__':

    number = int(input("Enter how many Numbers : "))
    total_sum = 0
    for i in range(1, number + 1):
        total_sum += float(input(f"Enter number #{i}: "))

    average = total_sum / number
    print(f"Average of {number} number is : {average}")
