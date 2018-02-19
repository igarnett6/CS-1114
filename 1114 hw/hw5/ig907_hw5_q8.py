lineText = input("Please enter a line of text: ");
char = input("Please enter the character you want to remove: ");
newText = '';


for i in lineText:
    if(i == char):
        newText += '';
    else:
        newText += i;
print(newText);