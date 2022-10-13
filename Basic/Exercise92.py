"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 01
       CSE, 2018, HSTU
"""


# Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict()
print("Method #01 : Looping ->")
for i in range(len(keys)):
    result[keys[i]] = values[i]
print(result)

dictionary = dict()
print("\nMethod #02 : zip()")
for key, value in zip(keys, values):
    dictionary[key] = value
print(dictionary)
