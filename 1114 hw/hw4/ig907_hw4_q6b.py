print("Please enter your sequence: ")
seq = int(1)
enter = 0
length = 0
while(enter != "done"):
    enter = input()
    if(enter != "done"):
        seq *= int(enter)
        length += 1
mean = seq**(1/length)
print("The geometric mean is: ", mean)