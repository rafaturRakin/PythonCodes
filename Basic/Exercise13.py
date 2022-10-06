"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 13
       CSE, 2018, HSTU
"""

# Print multiplication table form 1 to 10

for x in range(1, 11):
    print(x, end='\t')
    for i in range(2, 11):
        print(x * i, end=' ')
    print()
