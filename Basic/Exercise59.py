"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""


# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
def create_string(string1, string2):
    result = ""
    x = len(string1) - 1
    y = len(string2) - 1
    i = 0
    j = y
    while i <= x and j >= 0:
        result += string1[i] + string2[j]
        i += 1
        j -= 1

    if i <= x:
        result += string1[i:]

    if j >= 0:
        result += string2[j::-1]
    print(result)


create_string("Abcde", "Xyz")
