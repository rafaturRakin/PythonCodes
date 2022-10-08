"""
#Author     : Rakin
#Date       : 08-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Function Exercise
#Exercise   : 07
       CSE, 2018, HSTU
"""


# Assign a different name to function and call it through the new name
def display_student(name, age):
    print(f"Name: {name}, Age: {age}")


display_student("Rakin", 22)

show_student = display_student

show_student("Aditya", 21)
