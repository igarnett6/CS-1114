length = int(input("Please enter the length of the sequence: "))
print("Please enter your sequence: ")
seq = int(1)
for i in range(length):
    seq *= int(input())
mean = seq**(1/length)
print("The geometric mean is: ", mean)