"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 09
       CSE, 2018, HSTU
"""


# Write a program to check if the given number is a palindrome number.
def is_palindrome(num):
    x = num
    reverse = 0
    while x > 0:
        remainder = x % 10
        reverse = (10 * reverse) + remainder
        x = x // 10

    print("original number ", num)
    if num == reverse:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")


is_palindrome(121)
is_palindrome(1454)
