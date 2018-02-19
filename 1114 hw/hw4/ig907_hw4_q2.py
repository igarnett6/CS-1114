n = int(input("Enter a positive integer: "))
x = n-1;
y = 0;
for i in range(n):
    print(y*" ",x*"*", "*", x*"*", y*" ", sep = "")
    x-=1;
    y+=1;

x+=1;
y-=1;

for j in range (n):
    print(y * " ", x * "*", "*", x * "*", y * " ", sep="")
    x+=1;
    y-=1;