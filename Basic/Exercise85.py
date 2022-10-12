"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 04
       CSE, 2018, HSTU
"""


# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = list()

for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)

print("Output :", result)

print("\n Using list comprehension ->")
result= [x + y for x in list1 for y in list2]
print("Output :", result)