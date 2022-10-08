"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 02
       CSE, 2018, HSTU
"""


# Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    for x in args:
        print(x, end=' ')
    print()


func1(1, 2, 3, 4, 5)
func1(1, 2, 3)
func1(1)