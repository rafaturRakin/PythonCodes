"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 15
       CSE, 2018, HSTU
"""


# Remove special symbols / punctuation from a string

string = "/*Jon is @developer & musician"

previous = ''
for x in string:
    if x.isalpha() or x.isdigit() or x == ' ':
        continue
    string = string.replace(x, '')

new_string = list(filter(None, string.split(' ')))
print(' '.join(new_string))
