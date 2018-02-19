def circularShiftList1(lst, k):
    output = []
    for i in range(k, len(lst)):
        output.append(lst[i])
    for i in range(k):
        output.append(lst[i])
    return output

lst = [1,2,3,4,5]
k = 3

print(circularShiftList1(lst, k))