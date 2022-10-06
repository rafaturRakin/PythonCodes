"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 9
       CSE, 2018, HSTU
"""

# Check file is empty or not
import os
size = os.stat('new_file.txt').st_size
print("File is Empty") if size == 0 else print("File is not Empty")
