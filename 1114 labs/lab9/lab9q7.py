def removeBelowAvg(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    avg = sum/len(lst)
    for i in range(len(lst)):
        if(lst[i] < avg):
            lst.pop(i)
    return