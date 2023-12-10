"""
Python File handling :
----------------------
    1. File handling is an important part of any web application.

    2. Python has several functions for creating, reading, updating, and deleting files.
"""

print('File handling :')
print('---------------')
print("")

print("** File Open **")
print("---------------")
print("")


try:
    file = open("test.txt","r")
    print(file.read())

except FileNotFoundError:
    print("Error : the file is not in your folder")

else:
    file.close()
