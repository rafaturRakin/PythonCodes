"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 17
       CSE, 2018, HSTU
"""


# Find words with both alphabets and numbers
string = "Emma25 is Data scientist50 and AI Expert".split(' ')

# for word in string:
#     for char in word:
#         if char.isdigit():
#             print(word)
#             break

# second solution
for word in string:
    if any(char.isdigit() for char in word) and any(char.isalpha() for char in word):
        print(word)
