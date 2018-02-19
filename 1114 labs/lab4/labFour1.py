x = int(input("Please enter a positive integer: "))
n = int(input("Please enter the number of digits: "))
sum = int(0)
k = int(x)
count = int(1)
while(count <= n):
    sum+= x%10
    x = x//10
    count +=1



print("The sum of the last", n, "digits is", sum)