letter = input("Enter a character: ");

if(letter.isupper()):
    print(letter, "is an upper case letter.");
elif(letter.islower()):
    print(letter, "is a lower case letter.");
elif(letter.isnumeric()):
    print(letter, "is a digit.");
else:
    print(letter, "is a non-alphanumeric character.");