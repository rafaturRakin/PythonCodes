"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 8
       CSE, 2018, HSTU
"""

# Format variables using a string.format() method.
totalMoney = 1000
quantity = 3
price = 450

sentence = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."
print(sentence.format(totalMoney, quantity, price))
