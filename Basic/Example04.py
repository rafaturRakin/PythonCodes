"""
#Author     : Rakin
#Date       : 04-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Program    : if...elif..else and Logical Operator
       CSE, 2018, HSTU
"""

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
mark = int(input("Enter your marks: "))
c = 2

# if statement [even/odd]
print("Use of if...")
if a % 2 == 0:
    print("a is even")
if a % 2 == 1:
    print(f"a is odd")


# if...else statement [less than / greater than]
print("\nUse of if...else...")
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


# if...elif...else statement [GPA]
print("\nUse of if...elif...else...")
if 80 <= mark <= 100:
    print("GPA = 5.00 (A+)")
elif 70 <= mark <= 79:
    print("GPA = 4.00 (A)")
elif 60 <= mark <= 69:
    print("GPA = 3.50 (A-)")
elif 50 <= mark <= 59:
    print("GPA = 3.00 (B)")
elif 40 <= mark <= 49:
    print("GPA = 2.00 (C)")
elif 33 <= mark <= 39:
    print("GPA = 1.00 (D)")
else:
    print("GPA = 0.00 (F)")

# Nested if...else [sorting]
print("\nUse of nested if...else...")
if a > b and a > c:
    if b > c:
        print(f"a = {a}, b = {b}, c = {c}")
    else:
        print(f"a = {a}, c = {c}, b = {b}")
elif b > a and b > c:
    if a > c:
        print(f"b = {b}, a = {a}, c = {c}")
    else:
        print(f"b = {b}, c = {c}, a = {a}")
else:
    if a > b:
        print(f"c = {c}, a = {a}, b = {b}")
    else:
        print(f"c = {c}, b = {b}, a = {a}")

# Logical Operator
print("\nUse of logical operator")
if a > 0 and b > 0 and c > 0:
    print("All are positive number")
elif a > 0 or b > 0 or c > 0:
    print("At least 1 positive number")
else:
    print("All are negative number")
