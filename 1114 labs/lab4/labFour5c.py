n = int(input("Please enter a positive integer: "))
x = int(1)
sum = 0
while (x <= n):
    sum += x**3
    x+=1
print(sum)