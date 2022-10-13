"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""

# Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict.update({"location": sample_dict["city"]})
del sample_dict["city"]

# sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
