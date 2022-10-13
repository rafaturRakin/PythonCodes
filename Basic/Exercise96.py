"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 05
       CSE, 2018, HSTU
"""


# Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

result = dict()
for item in keys:
    result[item] = sample_dict.get(item)

print(result)

newDict = {k: sample_dict[k] for k in keys}
print(newDict)
