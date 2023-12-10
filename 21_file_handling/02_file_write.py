print('File handling :')
print('---------------')
print("")

print("** File write or overwrite in python **")
print("---------------------------------------")
print("")


try:
    file = open("test.txt","w")
    file.write("Hi this is change the test txt file")
    file.close()
    file = open("test.txt","r")
    print(file.read())
    
except FileNotFoundError:
    print("Error : the file is not in your folder")

else:
    file.close()
