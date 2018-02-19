n = int(input("Please enter a positive integer: "))
count = 1;
done = 0;
while(n != 0):
    if(count%2==0):
        print(count)
        n-=1;
    count+=1;

