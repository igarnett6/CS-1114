a = input("Enter string a: ")
b = input("Enter string b: ")

def afromb(a, b):
    if(len(a)>len(b)):
        return False
    else:
        bCopy = b
        start = 0
        for i in a:
            check = bCopy.find(i)
            if(check >= 0):
                bCopy = b[(check+1):]
            else:
                return False
    return True

print(afromb(a, b))


