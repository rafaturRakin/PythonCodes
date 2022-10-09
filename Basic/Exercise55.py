"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""


# Append new string in the middle of a given string
def append_in_middle(str1, str2):
    middle = len(s1) // 2
    str3 = str1[:middle] + str2 + str1[middle:]
    print("New string is :", str3)


s1 = "Army"
s2 = "Kelly"
append_in_middle(s1, s2)
