def findMaxAbsVal(lst):
    max = 0
    maxIndex = 0
    for i in range(len(lst)):
        if(abs(lst[i]) > max):
            max = abs(lst[i])
    return max

def main():
    lst = []
    length = int(input("Enter a length for the list: "))

    for i in range(length):
        add = int(input("Enter a value to add to the list: "))
        lst.append(add)
    output = findMaxAbsVal(lst)
    print("List: ", lst)
    print("The maximum absolute value is: ", output)
main()