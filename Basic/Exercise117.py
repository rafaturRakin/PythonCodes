"""
#Author     : Rakin
#Date       : 17-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Tuple Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""

# Modify the tuple

tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 222

print(tuple1)


temp = list(tuple1)

temp[1][0] = 222

tuple1 = tuple(temp)

print(tuple1)
