"""
#Author     : Rakin
#Date       : 04-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Program    : Relational Operators and Ternary Operator
       CSE, 2018, HSTU
"""

# Relational Operator
a = 5
b = 7

print(f"{a} < {b} = {a < b}")
print(f"{a} <= {b} = {a <= b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} >= {b} = {a >= b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}")
print()

# Ternary operator
# True_Statement if [condition] else False_Statement
print(f"a({a}) is greater than b({b})") if a > b \
    else print(f"a({a}) is less than b({b})")
