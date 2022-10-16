"""
#Author     : Rakin
#Date       : 16-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Set Exercise
#Exercise   : 05
       CSE, 2018, HSTU
"""

# Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
items_to_remove = [10, 20, 30]

set1.difference_update(items_to_remove)

print(set1)

