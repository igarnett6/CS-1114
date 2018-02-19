n = int(input("Enter a number n: "))
lst = []
for i in range(1, n+1):
    add = 2**i
    lst.append(add)
print("List: ",lst)