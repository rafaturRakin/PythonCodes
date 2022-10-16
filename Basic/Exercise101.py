"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 10
       CSE, 2018, HSTU
"""


# Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

employee = "Brad"

for item in sample_dict.values():
    if item["name"] == employee:
        item.update({"salary": 8500})

print(sample_dict)
