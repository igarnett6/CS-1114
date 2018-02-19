n = int(input("Enter a number: "))

def getCompliment(n):
    original = bin(n)
    output = ''
    for i in original:
        if(i == '1'):
            output += "0"
        if(i == '0'):
            output += "1"

    return int(output, 2)

print(getCompliment(n))
