expression = input("Enter a mathematical expression: ");
space1 = expression.find(' ');
newExp = expression[space1:];
space2 = space1 + 3;
firstNumber = expression[:space1]
secondNumber = expression[space2:]
if(expression[2]=='+'):
    output = int(firstNumber) + int(secondNumber);
elif(experssion[2]=='-'):
    output = int(firstNumber) - int(secondNumber);
else:
    output = int(firstNumber) / int(secondNumber);
print(expression,"=",output);
