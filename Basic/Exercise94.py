"""
#Author     : Rakin
#Date       : 13-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Dictionary Exercise
#Exercise   : 03
       CSE, 2018, HSTU
"""


# Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

value_of_history = sampleDict["class"]["student"]["marks"]["history"]
print(value_of_history)
