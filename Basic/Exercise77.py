"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""

# Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection_set = first_set & second_set
difference_set = first_set - intersection_set

print("Intersection set is", intersection_set)
print("First set after removing common elements", difference_set)