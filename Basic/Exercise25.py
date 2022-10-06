"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 10
       CSE, 2018, HSTU
"""

# Read line number 4 from the following file
file = open('test.txt', 'r')

lines = file.readlines()

print(lines[3]) if len(lines) >= 4 else print("Line not found")
