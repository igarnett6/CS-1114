letter = input("Enter a character: ");
if((96 <= ord(letter)<=123)):
    print(letter, "is a lower case letter.");
elif(ord(letter)>64 and ord(letter)<=90):\
    print(letter,"is an upper case character.");
elif(48<=ord(letter)<=57):
    print(letter, "is a digit.");
else:
    print(letter, "is a non-alphanumeric character.");