def getCommonElement(lst1, lst2):
    output = []
    if(len(lst1)>len(lst2)):
        length = len(lst1)
    else:
        length = len(lst2)
    for i in range(length):
        if(lst2.count(lst1[i]) != 0):
            output.append(lst1[i])
    return output

lst1 = [1,2,3,4]
lst2 = [2,4,6,8]

print(getCommonElement(lst1, lst2))