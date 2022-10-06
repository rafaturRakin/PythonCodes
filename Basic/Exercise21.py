"""
#Author     : Rakin
#Date       : 06-10-2022
#Language   : Python (3.10.5)
#IDE        : PyCharm
#Website    : Pynative
#Topic      : Input and Output Exercise
#Exercise   : 6
       CSE, 2018, HSTU
"""

# Write all content of a given file into a new file by skipping line number 5

readFile = open("test.txt", "r")
lines = readFile.readlines()
readFile.close()

counter = 0
writeFile = open("new_file.txt", "w")
for line in lines:
    counter += 1
    if counter == 4:
        continue
    writeFile.write(line)
writeFile.close()
