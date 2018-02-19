origStr = input("Please enter a string: ")
newStr = ""
for i in range(len(origStr)):
    if(origStr[i].isupper()):
        newStr+=origStr[i].lower()
    elif(origStr[i].islower()):
        newStr+=origStr[i].upper()
print("New string is: ", newStr)