num = str(1)
userNum = int(input("Enter a positive integer: "))
space = int(userNum+1)

for i in range(userNum+1):
    if(i > 0):
        num = str(i)
        print(space*" ", i*num)
    space -= 1

