"""
#Author     : Rakin
#Date       : 17-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Tuple Exercise
#Exercise   : 120
       CSE, 2018, HSTU
"""

# Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

length = len(tuple1)
elements = tuple1.count(tuple1[0])

print(length == elements)

print(all(i == tuple1[0] for i in tuple1))
