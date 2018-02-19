def sumSquareList(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]**2
    return sum

lst = [1,2,3,4,5]
print(sumSquareList(lst))