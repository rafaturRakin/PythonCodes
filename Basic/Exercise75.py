"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 04
       CSE, 2018, HSTU
"""

# Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dictionary_items = {}

for x in sample_list:
    if dictionary_items.get(x) is None:
        dictionary_items[x] = 1
    else:
        dictionary_items[x] += 1

print("Printing count of each item:", dictionary_items)
