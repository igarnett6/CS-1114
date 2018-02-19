num = str(1)
userNum = int(input("Enter a positive integer: "))
space = int(userNum+1)

for i in range(userNum+2):
    if(i > 1):
       print(" ", num)
       num += str(i)
    space -= 1
