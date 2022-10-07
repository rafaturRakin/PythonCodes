"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""

# Print list in reverse order using a loop
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])
