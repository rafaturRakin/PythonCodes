"""
#Author     : Rakin
#Date       : 07-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Loop Exercise
#Exercise   : 12
       CSE, 2018, HSTU
"""

# Display Fibonacci series up to 10 terms
first = 0
second = 1

for i in range(1, 11):
    print(first, end=' ')
    fibonacci = first + second
    first = second
    second= fibonacci
