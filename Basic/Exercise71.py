"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 18
       CSE, 2018, HSTU
"""

# Replace each special symbol with '#' in the following string

string = '/*Jon is @developer & musician!!'
new_string = string

for char in string:
    if char.isalpha() or char.isdigit() or char == ' ':
        continue
    new_string = new_string.replace(char, '#')

print(f"Old string : {string}")
print(f"New string : {new_string}")
