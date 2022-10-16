"""
#Author     : Rakin
#Date       : 16-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Set Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""

# Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)

print(set3)

print(set1 & set2)
