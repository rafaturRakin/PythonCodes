"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""


# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

print("Method #01: update() ->")
result = dict1.copy()
result.update(dict2)
print(result)

print("\nMethod #02: Looping ->")
result2 = dict1.copy()
for key, value in dict2.items():
    result2[key] = value
print(result2)

print("\nMethod #03: using {**, **} ->")
result3 = {**dict1, **dict2}
print(result3)
