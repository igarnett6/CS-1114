userInput = input("Enter a decimal number: ");
inputCopy = int(userInput);

countI = inputCopy%5;
countV = (inputCopy%10)/5;
countV = int(countV);
inputCopy = inputCopy//10;
countX = inputCopy%10;
inputCopy = inputCopy//10;
countC = inputCopy%10;
inputCopy = inputCopy//10;
countL = inputCopy%10;
inputCopy = inputCopy//10;
countD = inputCopy%10;
inputCopy = inputCopy//10;
countM = inputCopy%10;

if(countX > 4):
    countX = countX-5;
    countL +=1;
if(countL > 4):
    countL = countL-5;
    countC +=1;
if(countC > 4):
    countC = countC-5;
    countD +=1;
if(countD > 4):
    countD = countD-5;
    countM += 1;

output = (countM*"M" + countD*"D" + countC*"C" + countL*"L" + countX*"X" + countV*"V" + countI*"I")

print(userInput, "is", output);