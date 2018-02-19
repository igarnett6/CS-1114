def findAll(lst, val):
    output = []
    for i in range(len(lst)):
        if(lst[i] == val):
            output.append(i)
    return output


def main():
    lst = []
    length = int(input("Enter a length for the list: "))

    for i in range(length):
        add = input("Enter a value to add to the list: ")
        lst.append(add)
    find = input("Enter a value to search for: ")
    print(findAll(lst, find))


main()