"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 11
       CSE, 2018, HSTU
"""
import math

# Write a program to display all prime numbers within a range
start = int(input("Enter first number : "))
end = int(input("Enter last number : "))

print("Primes between %d and %d are : " %(start, end))
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                break
        else:
            print(num)
