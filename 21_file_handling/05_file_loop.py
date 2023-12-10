print('File handling :')
print('---------------')
print("")

print("** File line print looping in python **")
print("---------------------------------------")
print("")


try:
    file = open("read_line.txt","r")

    for line in file:
        print(line) 

except FileNotFoundError:
    print("Error : the file is not in your folder")

else:
    file.close()
