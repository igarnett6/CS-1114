def count(lst, item):
    output = 0
    for i in range(len(lst)):
        if(lst[i] == item):
            output += 1

    return output

def main():
    lst = [0, 32, 'a', '0', '4', 15, 'q', '0']
    item = input("Enter the item to search for: ")
    print("Number of occurrences:", count(lst, item))
main()