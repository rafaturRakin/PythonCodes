"""
#Author     : Rakin
#Date       : 16-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Set Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""

# Return a set of elements present in Set A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = (set1 - set2) | (set2 - set1)

print(set3)

print(set1.symmetric_difference(set2))
