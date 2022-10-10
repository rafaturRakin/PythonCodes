"""
#Author     : Rakin
#Date       : 10-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : String Exercise
#Exercise   : 09
       CSE, 2018, HSTU
"""


# Calculate the sum and average of the digits present in a string
string = "Pynative29@#8496"

total = 0
numbers = 0

for x in string:
    if x.isdigit():
        total += int(x)
        numbers += 1

print(f"Sum of the digits is : {total}, and Average is %.2f" %(total/numbers))
