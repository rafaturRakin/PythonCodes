"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 14
       CSE, 2018, HSTU
"""


# Remove empty strings from a list of strings
string_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list = []

for x in string_list:
    if x is None or x == "":
        continue
    new_list.append(x)

print(f"Original List : {string_list}")
print(f"New list : {new_list}")

# print(list((filter(None, string_list))))
