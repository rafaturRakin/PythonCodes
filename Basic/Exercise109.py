"""
#Author     : Rakin
#Date       : 16-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Set Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""

# Update set1 by adding items from set2, except common items

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Before :", set1)
set1.symmetric_difference_update(set2)
print("After :", set1)
