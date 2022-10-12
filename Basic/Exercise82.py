"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 01
       CSE, 2018, HSTU
"""


# Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
list2 = list1.copy()
print("Original list:", list1)


print("\nMethod #01: using reverse method ->")
list1.reverse()
print("list1.reverse() :", list1)

print("\nMethod #02: using list slicing ->")
print("list2[::-1] :", list2[::-1])

print("\nMethod #03: using builtin reversed() ->")
print("list(reversed(list2)) :", list(reversed(list2)))