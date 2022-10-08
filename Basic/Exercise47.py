"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 04
       CSE, 2018, HSTU
"""


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary=9000):
    print(f"Hi {name}, your salary is {salary}")


show_employee("Rakin")
show_employee("Doe", 780)
