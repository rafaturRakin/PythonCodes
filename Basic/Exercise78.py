"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""

# Checks if one set is a subset or superset of another set. If found, delete all elements from that set

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is a subset of Second set -", first_set.issubset(second_set))
print("Second set is a subset of First set -", second_set.issubset(first_set))

print()

print("First set is a superset of Second set -", first_set.issuperset(second_set))
print("Second set is a superset of First set -", second_set.issuperset(first_set))

print()

first_set.clear()

print("First set", first_set)
print("Second set", second_set)
