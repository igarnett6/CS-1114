def findMaxEvenIndex(lst):
    max = lst[0]
    maxIndex = -1
    for i in range(len(lst)):
        if(lst[i]%2 == 0 and lst[i] > max):
            max = lst[i]
            maxIndex = i
    return maxIndex
lst = [1, 2, 4, 89, 54, 78, 12]
print("Max index at: ", findMaxEvenIndex(lst))