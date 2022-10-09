"""
#Author     : Rakin
#Date       : 09-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 04
       CSE, 2018, HSTU
"""


# Arrange string characters such that lowercase letters should come first
def arrange_characters(string):
    lower, upper = ["", ""]
    for x in string:
        if x.islower():
            lower += x
        else:
            upper += x
    return lower + upper


print("Result is:", arrange_characters("PyNaTive"))
