"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""

# Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

first = sample_list[0:len(sample_list)//3]
second = sample_list[len(sample_list)//3:len(sample_list) - len(sample_list)//3]
third = sample_list[len(sample_list) - len(sample_list)//3:]

print("First chunk:", first)
print("After reversing:", first[::-1])

print("Second chunk:", second)
second.reverse()
print("After reversing:", second)

print("Third chunk:", third)
print("After reversing:", list(reversed(third)))
