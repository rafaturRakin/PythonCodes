"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 08
       CSE, 2018, HSTU
"""


#  Find all occurrences of a substring in a given string by ignoring the case
def count_occurrence(string, substring):
    return string.lower().count(substring.lower())


str1 = "Welcome to USA. usa awesome, isn't it?"
sub = "USA"
print(f"{sub} occurred : {count_occurrence(str1, sub)}")
