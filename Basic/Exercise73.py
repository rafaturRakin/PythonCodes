"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""


# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
def add_and_remove(l1):
    removed_item = l1[4]
    l1.remove(removed_item)
    print("After removing from index 4 :", l1)
    l1.insert(2, removed_item)
    print("After inserting in index 2 :", l1)
    l1.append(removed_item)
    print("After inserting at last  :", l1)


list1 = [34, 54, 67, 89, 11, 43, 94]
print("Original list is:", list1)

add_and_remove(list1)
