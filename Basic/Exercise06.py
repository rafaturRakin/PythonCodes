"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 06
       CSE, 2018, HSTU
"""


# Iterate the given list of numbers and print only those numbers which are divisible by 5
numbers = [10, 20, 30, 33, 46, 55]

print("Given list is ", numbers)
print("Divisible by 5")

for x in numbers:
    if x % 5 == 0:
        print(x)
