"""
#Author     : Rakin
#Date       : 12-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : List Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""


# Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)
