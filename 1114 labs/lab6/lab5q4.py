s = input("Please enter string s: ")
reversed = ''
tempWord = ''

for letter in s:
    if(letter == ' '):
       reversed += tempWord[::-1] + ' '
       tempWord = ''
    else:
        tempWord += letter
reversed += tempWord[::-1] + " "
print("Result: ", reversed)