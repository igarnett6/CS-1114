n = int(input("Enter a positive integer: "))
oddCount = 0
evenCount = 0
for i in range(n):

    if(i%2 == 0):
        evenCount+=1
    else:
        oddCount +=1
    if(evenCount > oddCount):
        print(i)

