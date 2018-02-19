ch = input("Enter a lowercase character: ")
n = int(input("Enter a positive value: "))

def wrap(ch, n):
    output = ''
    val = ord(ch)
    j = 0
    for i in range(n):
        check = val+j

        if(check <= 122):
            output += chr(val+j)
            j+=1
        else:
            val = 97
            j = 0
            output += chr(val+j)
            j+=1
    return output

print(wrap(ch, n))