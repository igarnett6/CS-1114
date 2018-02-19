num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

tNum1 = num1
tNum2 = num2
diffCount = 0

while(tNum1 != 0):

    comp1 = tNum1%10
    comp2 = tNum2%10
    if(comp1 != comp2):
        diffCount += 1
    tNum1 = tNum1//10
    tNum2 = tNum2//10


print("The Hamming Distance between", num1, "and", num2, "is: ", diffCount)
