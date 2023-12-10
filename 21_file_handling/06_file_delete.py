print('File handling :')
print('---------------')
print("")

print("** File Delte in python **")
print("--------------------------")
print("")



import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
    # os.rmdir("folder name") if want to delete a folder

else:
    print("File is not found")
