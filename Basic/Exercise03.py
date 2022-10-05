"""
#Author     : Rakin
#Date       : 05-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 03
       CSE, 2018, HSTU
"""

# Write a program to accept a string from the user and display characters that are present at an even index number.

text = input()

print("Original String is ", text)
length = len(text)

print("Printing only even index chars")
for i in range(length):
    if not (i % 2):
        print(text[i])