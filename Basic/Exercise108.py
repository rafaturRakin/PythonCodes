"""
#Author     : Rakin
#Date       : 16-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Set Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""

# Check if two sets have any elements in common. If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Two sets have no common element")
else:
    print("Common items:")
    print(set1.intersection(set2))
