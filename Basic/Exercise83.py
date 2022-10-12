"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""


# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = list()

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print("Resulted list :", result)

print("\nList comprehension with zip() ->")
result = [item1 + item2 for item1, item2 in zip(list1, list2)]
print("Resulted list :", result)