strA = input("Please enter string a: ")
strB = input("Please enter string b: ")
strLong = ''
strShort = ''
if(len(strA)> len(strB)):
    strLong += strA[:]
    strShort += strB[:]
else:
    strLong += strB[:]
    strShort += strA[:]

strNew = strShort + strLong + strShort
print("The output is: ", strNew)