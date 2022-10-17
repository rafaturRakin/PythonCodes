"""
#Author     : Rakin
#Date       : 17-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Tuple Exercise
#Exercise   : 118
       CSE, 2018, HSTU
"""


# Sort a tuple of tuples by 2nd item

def take_second(element):
    return element[1]


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

tuple1 = sorted(tuple1, key=take_second)

print(tuple(tuple1))
