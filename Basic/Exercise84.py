"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""


# Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
result = list()

print("Original list :", numbers)

print("\nMethod #01: Looping ->")
for item in numbers:
    result.append(item * item)
print("Result :", result)

print("\nMethod #02: map() ->")
result = list(map(lambda x: x*x, numbers))
print("Result is:", result)

print("\nMethod #03: list comprehension ->")
result = [item * item for item in numbers]
print("Result is:", result)