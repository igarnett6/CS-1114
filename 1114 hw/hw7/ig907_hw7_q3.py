def addList(lst1, lst2):
    length = len(lst1)
    output = []
    for i in range(length):
        sum = lst1[i]+lst2[i]
        output.append(sum)
    return output


def main():
    lst1 = []
    lst2 = []
    done = False
    print("List 1: ")
    while(done == False):
        add = input("Enter a value (done to end): ")
        if(add == "done"):
            done = True
        else:
            lst1.append(add)
    print("List 2: ")
    done = False
    while (done == False):
        add = input("Enter a value (done to end): ")
        if (add == "done"):
            done = True
        else:
            lst2.append(add)
    if(len(lst1) == len(lst2)):
        print("The list of sums: ", addList(lst1, lst2))
    else:
        print("The lists are different lengths.")



main()