"""
#Author     : Rakin
#Date       : 03-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Program    : User Input and Type Casting
       CSE, 2018, HSTU
"""

import math

# type casting
variable1 = input("Enter a text: ")
variable2 = int(input("Enter a number: "))
variable3 = bool(input("Enter True or False: "))
variable4 = 12.75

# use of type()
print()
print(f"variable1: type = {type(variable1)} & value = {variable1}")
print(f"variable2: type = {type(variable2)} & value = {variable2}")
print(f"variable3: type = {type(variable3)} & value = {variable3}")

# string operation
print()
print(f"{variable1} * 3 = {variable1 * 3}")
print(f"{variable1} + {variable1} = {variable1 + variable1}")

# math function

print()
print(f"pi = {math.pi}")
print(f"e = {math.e}")
print(f"infinity = {math.inf}")
print(f"nan = {math.nan}")
print(f"tau = {math.tau}")
print(f"{variable2}^7 = {math.pow(variable2, 7)}")
print(f"sqrt({variable2}) = {math.sqrt(variable2)}")
print(f"Floor of {variable4} = {math.floor(variable4)}")
print(f"Ceiling of {variable4} = {math.ceil(variable4)}")
print(f"Round of {variable4} = {round(variable4)}")