n = int(input("Please enter a positive integer: "))
sum = int(0)
count = int(1)
while(count <= n):
    if(count%2 != 0):
        print("+",count, end = '',sep = '')
        sum += count;
    else:
        print("-",count, end = '', sep = '')
        sum += -1*count;
    count+=1;



print("\nThe sum of the digits is", sum)