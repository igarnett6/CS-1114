userInput = input("Enter a number in the simplified Roman system: ");
countI = 0;
countV = 0;
countX = 0;
countL = 0;
countC = 0;
countD = 0;
countM = 0;
countInvalid = 0;

for i in range(len(userInput)):
    cChar = userInput[i];
    if(cChar == 'I'):
        countI +=1;
    elif(cChar == 'V'):
        countV += 1;
    elif(cChar == 'X'):
        countX += 1;
    elif(cChar == 'L'):
        countL += 1;
    elif(cChar == 'C'):
        countC += 1;
    elif(cChar == 'D'):
        countD += 1;
    elif(cChar == 'M'):
        countM += 1;
    else:
        countInvalid += 1;
output = (countI*1) + (countV*5) + (countX*10) + (countL * 50) + (countC*100) + (countD*500) + (countM*1000);
print(userInput, "is", output)