def createPrefixLists(lst):
    length = len(lst)
    output = []
    for i in range(length):
        add = []
        for j in range(length):
            add.append(lst[j])
        output.append(add)
    return output
