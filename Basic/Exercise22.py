"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 7
       CSE, 2018, HSTU
"""

# Accept any three string from one input() call
names = input("Enter 3 names (separated by space) : ").split()

for i in range(0, 3):
    print(f"Name{i+1}: {names[i]}")
