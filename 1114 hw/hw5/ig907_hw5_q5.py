password = input("Enter a password: ");
countUpper = 0;
countLower = 0;
countNum = 0;
countRan = 0;
for i in range(len(password)):
    currChar = password[i];
    if(currChar.isupper()):
        countUpper+=1;
    elif(currChar.islower()):
        countLower +=1;
    elif(currChar.isnumeric()):
        countNum +=1;
    else:
        countRan += 1;

if(countUpper >= 2 and countLower >= 1 and countNum >= 2 and countRan > 0 and len(password) >= 8):
    print(password, "is a valid paassword");
else:
    print(password, "is not a valid password");