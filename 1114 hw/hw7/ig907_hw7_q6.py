def reverseToNewList(lst):
    output = []
    for i in range(len(lst)-1, -1, -1):
        output.append(lst[i])
    return output

def reverseInPlace(lst):
    revList = reverseToNewList(lst)
    for i in range(len(lst)):
        lst[i] = revList[i]
    return lst

def main():
     lst1 = [1, 2, 3, 4, 5, 6]
     rev_lst1 = reverseToNewList(lst1)
     print("After reverse_to_new_list, lst1 is", lst1,
    "and the returned list is", rev_lst1)

     lst2 = [1, 2, 3, 4, 5, 6]
     print("Before reverse_in_place, lst2 is", lst2)
     reverseInPlace(lst2)
     print("After reverse_in_place, lst2 is", lst2)
main()