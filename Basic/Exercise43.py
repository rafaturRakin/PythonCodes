"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 18
       CSE, 2018, HSTU
"""

# Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

num = int(input("Enter number : "))

for i in range(num):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(num-1):
    for j in range(num-i-1, 0, -1):
        print('*', end=' ')
    print()