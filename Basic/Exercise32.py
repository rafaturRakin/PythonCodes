"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""

# Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
