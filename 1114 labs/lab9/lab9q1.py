def fromNumber(n, myint):
    output = []
    for i in range(n):
        output.append(myint+i)
    return output

def main():
    myInt = int(input("Enter a positive integer: "))
    n = int(input("Enter a number n: "))
    print("Returned list: ", fromNumber(n, myInt))
main()


#a) ['hi', 'mom', 'dad'][1, 57, 15]
#b)hi 15
#c) ['hi', 'mom', 'dad', [1, 57, 15]]
#d) = ['hi','mom','dad']

#a) 5
#b) 3
#c) [3,4,5,6,4,5,6,7,5,6,7,8]