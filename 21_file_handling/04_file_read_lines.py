print('File handling :')
print('---------------')
print("")

print("** File Read line and Read lines **")
print("-----------------------------------")
print("")



try:
    file = open("read_line.txt","r")
    print(file.read())
   # print(file.readline())
   # print(file.readline(5))
   # print(file.readlines())

except FileNotFoundError:
    print("Error : the file is not in your folder")

else:
    file.close()
