"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 06
       CSE, 2018, HSTU
"""


# Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("Original list :", list1)

print("\nMethod #01: Using loop ->")
temp = list1.copy()
x = temp.count("")
for i in range(x):
    temp.remove("")
print(temp)

print("\nMethod #02: Using list comprehension ->")
result = [item for item in list1 if item.isalnum()]
print(result)

print("\nMethod #03: Using filter() ->")
result = list(filter(None, list1))
print(result)