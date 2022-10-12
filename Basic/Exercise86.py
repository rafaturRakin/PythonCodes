"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 05
       CSE, 2018, HSTU
"""


# Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, list2[::-1]):
    print(item1, item2)

print("\nMethod #02: looping ->")
length = len(list1)
for i in range(length):
    print(list1[i], list2[length - 1 - i])
