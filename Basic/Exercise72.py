"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 01
       CSE, 2018, HSTU
"""


# Create a list by picking an odd-index items from the first list and even index items from the second
def list_create(l1, l2):
    first = [l1[i] for i in range(1, len(l1), 2)]
    second = [l2[i] for i in range(0, len(l2), 2)]

    print("Element at odd index in list1 is: ")
    print(first)

    print("Element at even index in list2 is: ")
    print(second)

    print("Printing Final third list: ")
    print(first + second)


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list_create(list1, list2)
