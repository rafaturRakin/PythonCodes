"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""


# Create a new string made of the first, middle, and last characters of each input string
def crate_string(str1, str2):
    result = str1[0] + str2[0] + str1[len(str1)//2] + str2[len(str2)//2] + str1[-1] + str2[-1]
    return result


s1 = "America"
s2 = "Japan"
print("Created string is:", crate_string(s1, s2))
