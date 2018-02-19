n = int(input("Please enter a positive integer: "))
for k in range(n):
    for i in range(n):
        if(i == k):
            print('o', end = "")
        else:
            print('x',end = "")
    print("\n")
    i+=1
k+=1