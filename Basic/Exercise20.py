"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 5
       CSE, 2018, HSTU
"""

# Accept a list of 5 float numbers as an input from the user

myList = []
for i in range(0, 5):
    x = float(input(f"Enter element at index {i}: "))
    myList.append(x)

print(myList)
