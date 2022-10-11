"""
#Author     : Rakin
#Date       : 11-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Data Structure Exercise
#Exercise   : 10
       CSE, 2018, HSTU
"""

# Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_list = list(set(sample_list))
unique_tuple = tuple(unique_list)

print("List:", unique_list)
print("Tuple:", unique_tuple)
print("Min:", min(unique_tuple))
print("Max:", max(unique_tuple))
