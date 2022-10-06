"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Basic exercise for beginners
#Exercise   : 12
       CSE, 2018, HSTU
"""


# Calculate income tax for the given income by adhering to the below rules.
def calculate_interest(income):
    if income <= 10000:
        interest = 0.0
    elif income <= 20000:
        interest = (income - 10000) * .10
    else:
        interest = 10000 * 0.10
        interest += (income - 20000) * .20

    print("Total interest is : ", interest)


calculate_interest(45000)
